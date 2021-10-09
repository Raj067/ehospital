from django.urls import path
from .views import *

doctor_urls = [
    path('doctor/', dashboard, name='dashboard'),
    path('doctor/admitted-patient/', admitted_patient, name='admitted_patient'),
    path('doctor/outpatient/patient/',
         outpatient_patient, name='outpatient_patient'),
    path('doctor/report/', report, name='report'),
]
