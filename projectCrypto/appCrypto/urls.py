# coincap_app/urls.py

from django.urls import path
from .views import coin_list

urlpatterns = [
    path('', coin_list, name='coin_list'),
]
