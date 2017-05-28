# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext as _


class OrderStatusEnum(object):
    """
    Статусы заявок
    """
    OPEN, CLOSED, PROCESSING, POSTPONED, UPDATE = range(5)

    values = {
        OPEN: _('Открыта'),
        CLOSED: _("Закрыта"),
        PROCESSING: _("Выполняеется"),
        POSTPONED: _("Отложена"),
        UPDATE: _("Уточение"),
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
        return "__".join((self.street, self.number))

    @cached_property
    def address(self):
        return 'ул. {}, дом {}'.format(self.street, self.number)


class Chat(models.Model):
    """Чат для дома"""
    name = models.CharField(_("Имя чата"), max_length=55)
    link = models.CharField(_("ссылка"), max_length=400)
    house = models.OneToOneField(
        House, on_delete=models.CASCADE, null=True, blank=True)
    telegram_chat_id = models.CharField('ID телеграм чата',
                                        max_length=100,
                                        null=True, blank=True)
    telegram_chat_title = models.CharField('название чатика в Telegram',
                                           max_length=100,
                                           null=True, blank=True)

    def __str__(self):
        return self.name

    @cached_property
    def house_address(self):
        if self.house:
            return self.house.address


class Order(models.Model):
    chat = models.ForeignKey(Chat, verbose_name=u'Из какого чата')
    status = models.SmallIntegerField(
        _("Состояние запроса"), choices=OrderStatusEnum.values.items(),
        default=OrderStatusEnum.OPEN)
    text = models.TextField('Текст заявки')
    executor = models.CharField('Исполнитель', max_length=200,
                                null=True, blank=True)
    created = models.DateTimeField('Время создания', auto_now_add=True)
    finished = models.DateTimeField('Время исполнения', null=True, blank=True)

    def display(self):
        return u"{} {}".format(
            self.id, OrderStatusEnum.values.get(self.status))

    def __str__(self):
        return self.display()
