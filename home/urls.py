from django.urls import path
from home.views import HomeView, Find_usView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    ]