# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from django.db import models


class AssociationOwnerHousing(models.Model):
    """Товарищество Собственников Жилья """
    name = models.CharField(_("Название ТСЖ"), max_length=40)
    inn = models.CharField(_("ИНН"), max_length=40)
    kpp = models.CharField(_("КПП"), max_length=40)


class ModeratorUser(User):
    """ Модераторы """
    association_owner_housing = models.ForeignKey(
        AssociationOwnerHousing, verbose_name=_(u'ТСЖ'), db_index=True)


class House(models.Model):
    """ Дом """
    street = models.CharField(_("Улица"), max_length=40)
    house = models.CharField(_("Дом"), max_length=40)
    post_index = models.CharField(_("Почтовый Индекс"), max_length=40)
    city = models.CharField(_("Город"), max_length=40)


class Chat(models.Model):
    """Чат"""
    link = models.CharField(_("Улица"), max_length=160)
    chat = models.OneToOneField(
        House, on_delete=models.CASCADE, primary_key=True)


class ModeratorRequest(models.Model):
    """Запрос модератора"""