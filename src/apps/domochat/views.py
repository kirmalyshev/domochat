from django.shortcuts import render_to_response, get_object_or_404

from apps.domochat.models import HOA, Order
from apps.domochat.models import House


def hoa_view(request, name=None):
    if name:
        # В тестовом не будет имен с одинаковыми названиями
        company = HOA.objects.filter(name=name).get()
        houses = House.objects.filter(
            hoa=company
        ).select_related('hoa')

    return render_to_response(
        'hoa.html', locals())


def index_view(request):
    return render_to_response(
        'hoa.html', locals())


def profile_view(request, name=None):
    company = HOA.objects.filter(name=name).get()
    houses = House.objects.filter(
        hoa=company
    ).select_related('hoa')

    return render_to_response(
        'profile_view.html', locals())


def order_item_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    context = {
        'order': order
    }

    return render_to_response('order_item.html', context=context)


def order_list_view(request):
    orders = Order.objects.all()

    context = {
        'orders': orders
    }
    return render_to_response('order_list.html', context=context)
