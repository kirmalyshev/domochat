# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext as _


class PositionEnum(object):
    """
    Статусы заявок
    """
    CLOSED, IN_PROCESSING, POSTPONED, UPDATE, REOPENED = range(0, 5)

    values = {
        CLOSED: _("Закрыта"),
        IN_PROCESSING: _("Выполняеется"),
        POSTPONED: _("Отложена"),
        UPDATE: _("Уточение"),
        REOPENED: _("Пере окрыта"),
    }


class HOA(models.Model):
    """Товарищество Собственников Жилья - House Owners Association"""
    name = models.CharField(_("Название ТСЖ"), max_length=40)
    inn = models.CharField(_("ИНН"), max_length=40,
                           null=True, blank=True)
    kpp = models.CharField(_("КПП"), max_length=40,
                           null=True, blank=True)

    def __str__(self):
        return self.name


class ModeratorUser(User):
    """ Модераторы """
    association_owner_housing = models.ForeignKey(
        HOA, verbose_name=_(u'ТСЖ'), db_index=True)


class ModeratorRequest(models.Model):
    """Запрос модератора"""
    status = models.SmallIntegerField(
        _("Состояние запроса"), choices=PositionEnum.values.items())
    text = models.TextField(_("Текс заявки"))

    def display(self):
        return u"{} {}".format(self.id, PositionEnum.values.get(self.status))

    def __str__(self):
        return self.display()


class House(models.Model):
    """ Дом """
    street = models.CharField(_("Улица"), max_length=40)
    number = models.CharField(_("Дом"), max_length=40)
    post_index = models.CharField(_("Почтовый Индекс"), max_length=40,
                                  null=True, blank=True)
    city = models.CharField(_("Город"), max_length=40)
    hoa = models.ForeignKey(
        HOA,
        verbose_name=_(u'ТСЖ'), db_index=True, null=True, blank=True)

    def __str__(self):
        return "__".join((self.street, self.house_num))


class Chat(models.Model):
    """Чат для дома"""
    name = models.CharField(_("Имя чата"), max_length=55)
    link = models.CharField(_("ссылка"), max_length=400)
    house = models.OneToOneField(
        House, on_delete=models.CASCADE, primary_key=True)
    request = models.ForeignKey(
        ModeratorRequest, related_name='get_moderators',
        verbose_name=_(u'Заявка'), db_index=True, null=True, blank=True)

    def __str__(self):
        return self.name

    @cached_property
    def house_address(self):
        if self.house:
            return self.house.address()


class Order(models.Model):
    chat = models.ForeignKey(Chat, verbose_name=u'Из какого чата')
    text = models.TextField('Текст заявки')
    executor = models.CharField('Исполнитель', max_length=200)
    created = models.DateTimeField('Время создания', auto_now_add=True)
    finished = models.DateTimeField('Время исполнения', null=True, blank=True)
