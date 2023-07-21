from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from .models import Variant, Duration, OrderModel


class HomeView(TemplateView):
    """
    View to render homepage
    """
    template_name = 'home/index.html'

class Order(View):
    def get(self, request, *args, **kwargs):
        # get every Variant from each duration
        fullDay = Variant.objects.filter(
            category__name__contains='Full Day')
        halfDay = Variant.objects.filter(category__name__contains='Half Day')
        hourlyBase = Variant.objects.filter(category__name__contains='Hourly Base')

        # pass into context
        context = {
            'Full Day': fullDay,
            'Half Day': halfDay,
            'Hourly Base': hourlyBase,
        }

        # render the template
        return render(request, 'home/order.html', context) # Make sure to edit this template.

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = Variant.objects.get(pk__contains=int(item))
            item_data = {
                'id': variant_item.pk,
                'name': variant_item.name,
                'price': variant_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'home/index.html', context)