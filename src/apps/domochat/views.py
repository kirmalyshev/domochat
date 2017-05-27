from django.http import Http404
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _

from apps.domochat.models import AssociationOwnerHousing
from apps.domochat.models import House


def main_page(request, name=None):

    if name:
        # В тестовом не будет имен с одинаковыми названиями
        company = AssociationOwnerHousing.objects.filter(name=name).get()
        houses = House.objects.filter(
            association_owner_housing=company
        ).select_related('chat')

    return render_to_response(
        'main_page.html', locals())



