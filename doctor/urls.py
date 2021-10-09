from django.urls import path
from .views import *

doctor_urls = [
    path('doctor/', dashboard, name='dashboard'),
    path('doctor/admitted-patient/', admitted_patient, name='admitted_patient'),
    path('doctor/outpatient/patient/',
         outpatient_patient, name='outpatient_patient'),
    path('doctor/report/', report, name='report'),
    path('doctor/complaints/', complaints, name='complaints'),
    path('doctor/medication-completed/',
         medication_completed, name='medication_completed'),
    path('doctor/medication-request/',
         medication_request, name='medication_request'),
    path('doctor/medication-new/',
         medication_new, name='medication_new'),
    path('doctor/imaging-completed/', imaging_completed, name='imaging_completed'),
    path('doctor/imaging-request/', imaging_request, name='imaging_request'),
    path('doctor/all-schedule/', all_schedule, name='all_schedule'),
    path('doctor/today-schedule/', today_schedule, name='today_schedule'),
    path('doctor/add-schedule/', add_schedule, name='add_schedule'),
    path('doctor/theater-schedule/', theater_schedule, name='theater_schedule'),
    path('doctor/add-theater-schedule/',
         add_theater_schedule, name='add_theater_schedule'),
]
