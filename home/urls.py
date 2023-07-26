from django.urls import path
from home.views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_order', views.createOrder, name='create_order'),
    path('profile', views.profile, name='profile'),
    path('order/<int:pk>/', views.update_order, name='update-order'),
    path('edit/<int:pk>/', views.edit_order, name='edit_order'),

    ]