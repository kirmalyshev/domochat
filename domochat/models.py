# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _

from django.db import models


class AssociationOwnerHousing(models.Model):
    """Товарищество Собственников Жилья """
    name = models.CharField(_("Название ТСЖ"), max_length=40)
    inn = models.PositiveIntegerField(_("ИНН"))
    kpp = models.PositiveIntegerField(_("КПП"))


class ModeratorUser(User):
    """ Модераторы """
    models.ForeignKey(
        AssociationOwnerHousing, verbose_name=_(u'отдел'), null=True,
        blank=True, db_index=True
    )

