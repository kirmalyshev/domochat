from django.shortcuts import render_to_response

from apps.domochat.models import HOA
from apps.domochat.models import House


def main_page(request, name=None):
    if name:
        # В тестовом не будет имен с одинаковыми названиями
        company = HOA.objects.filter(name=name).get()
        houses = House.objects.filter(
            hoa=company
        ).select_related('hoa')

    return render_to_response(
        'main_page.html', locals())


def profile_page(request, name=None):
    company = HOA.objects.filter(name=name).get()
    houses = House.objects.filter(
        hoa=company
    ).select_related('hoa')

    return render_to_response(
        'index.html', locals())