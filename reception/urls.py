from django.urls import path
from .views import *

reception_urls = [
    path('reception/', dashboard, name='dashboard'),
]
