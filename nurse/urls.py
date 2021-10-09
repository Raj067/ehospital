from django.urls import path
from .views import *

nurse_urls = [
    path('nurse/', dashboard, name='dashboard'),
    path('nurse/all_schedule/', all_schedule, name='all_schedule'),
    path('nurse/today_schedule/', today_schedule, name='today_schedule'),
    path('nurse/add_schedule/', add_schedule, name='add_schedule'),
    path('nurse/theater_schedule/', theater_schedule, name='theater_schedule'),
    path('nurse/theater_schedule/', add_theater_schedule, name='theater_schedule'),
]
