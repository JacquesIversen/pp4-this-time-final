from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from home.models import OrderModel


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year,
            created_on__month=today.month,
            created_on__day=today.day)

        # loop through the orders and add the price value
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

        # pass total number of orders and total revenue into template
        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, 'staff/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


def change_status(request, pk):
    print(pk)

    order = OrderModel.objects.get(pk=pk)
    if request.method == 'POST':

        status = request.POST.get('status')
        print(status)
        if status:
            order.status = status
            order.save()

    return redirect('dashboard')
