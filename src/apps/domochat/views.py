from django.shortcuts import render_to_response, get_object_or_404

from apps.domochat.models import HOA, Order
from apps.domochat.models import House


def index_view(request, name=None):
    if name:
        # В тестовом не будет имен с одинаковыми названиями
        company = HOA.objects.filter(name=name).get()
        houses = House.objects.filter(
            association_owner_housing=company
        ).select_related('chat')

    return render_to_response('index.html', locals())


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
