from django.shortcuts import render, redirect

# Create your views here.


def home(request, *args, **kwargs):
    txt = 0
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email in ['admin.demo@hospitalini.com', 'office.demo@hospitalini.com',
                     'doctor.demo@hospitalini.com', 'nurse.demo@hospitalini.com']:
            if email == 'admin.demo@hospitalini.com':
                return redirect('/administrator/')
            elif email == 'office.demo@hospitalini.com':
                return redirect('/accounting/')
            elif email == 'doctor.demo@hospitalini.com':
                return redirect('/doctor/')
            elif email == 'nurse.demo@hospitalini.com':
                return redirect('/nurse/')
        else:
            txt = 'Invalid username or password'
    return render(request, 'home/home.html', {'txt':txt})

def dashboard(request, *args, **kwargs):
    return render(request, 'hr/home.html', {})
