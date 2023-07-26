from django.urls import path
from .views import Dashboard, change_status


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('dashboard/<int:pk>/', change_status, name='change_status'),
]