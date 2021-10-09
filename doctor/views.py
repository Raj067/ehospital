from django.shortcuts import render

# Create your views here.
def dashboard(request, *args, **kwargs):
    users = []
    data={
        'data': users
    }
    return render(request, 'doctor/home.html', data)
