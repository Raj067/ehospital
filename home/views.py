from django.shortcuts import render

# Create your views here.


def home(request, *args, **kwargs):
    return render(request, 'home/home.html', {})

def dashboard(request, *args, **kwargs):
    return render(request, 'hr/home.html', {})
