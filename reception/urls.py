from django.urls import path
from .views import *

reception_urls = [
    path('reception/', dashboard, name='dashboard'),
    path('reception/noinsurance/', noinsurance, name='noinsurance'),
    path('reception/insurance/', insurance, name='insurance'),
    path('reception/patients/', patients, name='patients'),
    path('reception/payments/', payments, name='payments'),
    path('reception/complaints/', complaints, name='complaints'),
]
