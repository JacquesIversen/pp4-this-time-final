from django.contrib import admin
from .models import Variant, Duration, OrderModel

# Register your models here.
admin.site.register(Variant)
admin.site.register(Duration)
admin.site.register(OrderModel)
