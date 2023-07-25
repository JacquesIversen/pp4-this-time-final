from django.urls import path
from home.views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_order', views.createOrder, name='create_order'),
    path('profile', views.profile, name='profile'),
    ]