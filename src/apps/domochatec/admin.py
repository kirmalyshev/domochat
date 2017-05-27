# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import (
    House, ModeratorUser, Chat, ModeratorRequest)

admin.site.register(House)
admin.site.register(ModeratorUser)
admin.site.register(Chat)
admin.site.register(ModeratorRequest)
