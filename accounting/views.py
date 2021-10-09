from django.shortcuts import render

# Create your views here.
def complaints(request, *args, **kwargs):
    return render(request, 'accounting/home.html', {})