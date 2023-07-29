from django.db import models
from django.contrib.auth import get_user_model


class Variant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='variants_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    STATUS = (
        ('Awaiting Pickup', 'Awaiting Pickup'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    items = models.ManyToManyField(
        'Variant', related_name='order', blank=True)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
