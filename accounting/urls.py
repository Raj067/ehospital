from django.urls import path
from .views import *

accounting_urls = [
    path('accounting/', home, name='dashboard'),
    path('accounting/admitted-patient/', admitted_patient, name='admitted_patient'),
    path('accounting/outpatient/patient/',
         outpatient_patient, name='outpatient_patient'),
    path('accounting/report/', report, name='report'),
    path('accounting/complaints/', complaints, name='complaints'),
    path('accounting/all-schedule/', all_schedule, name='all_schedule'),
    path('accounting/today-schedule/', today_schedule, name='today_schedule'),
    path('accounting/add-schedule/', add_schedule, name='add_schedule'),
    path('accounting/theater-schedule/', theater_schedule, name='theater_schedule'),
    path('accounting/add-theater-schedule/',
         add_theater_schedule, name='add_theater_schedule'),

    path('accounting/invoice/', invoice, name='invoice'),
    path('accounting/new-invoice/', new_invoice, name='new_invoice'),
    path('accounting/price/', price, name='price'),
    path('accounting/price-profile/', price_profile, name='price_profile'),
]
