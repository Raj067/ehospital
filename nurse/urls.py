from django.urls import path
from .views import *

nurse_urls = [
    path('nurse/', dashboard, name='dashboard'),
]
