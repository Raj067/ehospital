from django.shortcuts import render, redirect

# Create your views here.


def home(request, *args, **kwargs):
    txt = 0
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email in ['admin.demo@hmis.com', 'office.demo@hmis.com',
                     'doctor.demo@hmis.com', 'nurse.demo@hmis.com']:
            if email == 'admin.demo@hmis.com':
                return redirect('/administrator/')
            elif email == 'office.demo@hmis.com':
                return redirect('/accounting/')
            elif email == 'doctor.demo@hmis.com':
                return redirect('/doctor/')
            elif email == 'nurse.demo@hmis.com':
                return redirect('/nurse/')
        else:
            txt = 'Invalid username or password'
    return render(request, 'home/home.html', {'txt':txt})

def dashboard(request, *args, **kwargs):
    return render(request, 'hr/home.html', {})
