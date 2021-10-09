from django.urls import path
from .views import *

nurse_urls = [
    path('nurse/', dashboard, name='dashboard'),
    path('nurse/all-schedule/', all_schedule, name='all_schedule'),
    path('nurse/today-schedule/', today_schedule, name='today_schedule'),
    path('nurse/add-schedule/', add_schedule, name='add_schedule'),
    path('nurse/theater-schedule/', theater_schedule, name='theater_schedule'),
    path('nurse/add-theater-schedule/',
         add_theater_schedule, name='add_theater_schedule'),
    path('nurse/medication_completed/', medication_completed,
         name='medication_completed'),
    path('nurse/medication/requests/', medication_requests,
         name='dashmedication/requestsboard'),
    path('nurse/report/', report, name='report'),
    path('nurse/complaints/', complaints, name='complaints'),
]
