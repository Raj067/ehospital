"""ehospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.urls import home_urls
from accounting.urls import accounting_urls
from doctor.urls import doctor_urls
from nurse.urls import nurse_urls
from pharmacy.urls import pharmacy_urls
from reception.urls import reception_urls
from administrator.urls import administrator_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += home_urls + accounting_urls + doctor_urls + nurse_urls

urlpatterns += pharmacy_urls + reception_urls + administrator_urls
