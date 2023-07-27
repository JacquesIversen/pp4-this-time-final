from django.views.generic import TemplateView
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
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
            try:
                numpeople = int(people[index])
            except ValueError:
                numpeople = 1
            item_data = {
                'id': variant_item.pk,
                'name': variant_item.name,
                'price': variant_item.price * numpeople
                

            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        if items: 

            order = OrderModel.objects.create(price=price, user=request.user)
            order.items.add(*item_ids)
            

            context = {
                'items': order_items['items'],
                'price': price 
            }

            return render(request, 'home/order_confirmation.html', context)
        else: 
            return redirect('order')

        
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

    my_orders = OrderModel.objects.filter(user=user)

    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if email:
            user.email = email
            user.save()
        if username:
            user.username = username
            user.save()
        if first_name:
            user.first_name = first_name
            user.save()
        if last_name:
            user.last_name = last_name
            user.save()

    context = {
        'user_my_site': user,
        'my_orders': my_orders
    }

    return render(request, 'home/profile.html', context)


def update_order(request, pk):

    order = OrderModel.objects.get(pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('profile')

    context = {
        'order': order,
    }

    return render(request, 'home/order_detail.html', context)


def edit_order(request, pk):
        
    order = OrderModel.objects.get(pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('order')

    context = {
        'order': order,
    }

    return render(request, 'home/order_detail.html', context)


def faq(request):
    return render(request, 'home/faq.html')


def contact_success(request):
    print("Hahaha, We dont care about their claim")
    return render(request, 'home/contact_success.html')
