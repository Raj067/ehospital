from django.shortcuts import render

# Create your views here.


def dashboard(request, *args, **kwargs):
    return render(request, 'reception/home.html', {})

def insurance(request, *args, **kwargs):
    return render(request, 'reception/insurance.html', {})


def noinsurance(request, *args, **kwargs):
    return render(request, 'reception/noinsurance.html', {})


def patients(request, *args, **kwargs):
    return render(request, 'reception/patients.html', {})

def payments(request, *args, **kwargs):
    return render(request, 'reception/payments.html', {})


def complaints(request, *args, **kwargs):
    return render(request, 'reception/complaints.html', {})
