# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from django.db import models


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

class AssociationOwnerHousing(models.Model):
    """Товарищество Собственников Жилья """
    name = models.CharField(_("Название ТСЖ"), max_length=40)
    inn = models.CharField(_("ИНН"), max_length=40)
    kpp = models.CharField(_("КПП"), max_length=40)


class ModeratorUser(User):
    """ Модераторы """
    association_owner_housing = models.ForeignKey(
        AssociationOwnerHousing, verbose_name=_(u'ТСЖ'), db_index=True)


class ModeratorRequest(models.Model):
    """Запрос модератора"""
    status = models.SmallIntegerField(
        _("Состояние запроса"), choices=PositionEnum.values.items())
    text = models.TextField(_("Текс заявки"))


class House(models.Model):
    """ Дом """
    street = models.CharField(_("Улица"), max_length=40)
    house = models.CharField(_("Дом"), max_length=40)
    post_index = models.CharField(_("Почтовый Индекс"), max_length=40)
    city = models.CharField(_("Город"), max_length=40)
    association_owner_housing = models.ForeignKey(
        AssociationOwnerHousing, verbose_name=_(u'ТСЖ'), db_index=True)


class Chat(models.Model):
    """Чат"""
    name = models.CharField(_("Имя чата"), max_length=40)
    link = models.CharField(_("ссылка"), max_length=160)
    chat = models.OneToOneField(
        House, on_delete=models.CASCADE, primary_key=True)
    request = models.ForeignKey(
        ModeratorRequest, verbose_name=_(u'Заявка'), db_index=True)

