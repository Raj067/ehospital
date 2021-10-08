from django.urls import path
from .views import *

home_urls = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard' ),
]
