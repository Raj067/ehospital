from django.urls import path
from .views import *

doctor_urls = [
        path('doctor/', dashboard, name='dashboard'),
]
