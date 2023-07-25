from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Variant, OrderModel
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    """
    View to render homepage
    """
    template_name = 'home/index.html'


class Order(View):
    def get(self, request, *args, **kwargs):
        variants = Variant.objects.all()

        # pass into context
        context = {
            'variants': variants,
        }

        # render the template
        return render(request, 'home/order.html', context) # Make sure to edit this template.

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')
        people = request.POST.getlist('people[]')

        for index, item in enumerate(items):
            variant_item = Variant.objects.get(pk__contains=int(item))
            item_data = {
                'id': variant_item.pk,
                'name': variant_item.name,
                'price': variant_item.price * int(people[index])

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

        return render(request, 'home/order_confirmation.html', context)

        
class Pricing(View):
    def get(self, request, *args, **kwargs):
        variant_items = Variant.objects.all()

        context = {
            'variant_items': variant_items
        }

        return render(request, 'home/pricing.html', context)


def createOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        # print('printing post', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'home/order_form.html', context)


@login_required
def profile(request):
    user = request.user
    print(user.email)
    context = {'user_my_site':user}
    return render(request, 'home/profile.html', context)
