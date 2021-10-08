from django.shortcuts import render

# Create your views here.


def dashboard(request, *args, **kwargs):
    return render(request, 'reception/home.html', {})

def insurance(request, *args, **kwargs):
    return render(request, 'reception/insurance.html', {})


def noinsurance(request, *args, **kwargs):
    return render(request, 'reception/noinsurance.html', {})


def patients(request, *args, **kwargs):
    users = [
        ['Rajabu Mrisho', 25, 'Male', 49, '23/56', '0679190720'],
        ['Salehe Mrisho', 40, 'Male', 89, '90/45', '0679190720'],
        ['Jamila Mrisho', 40, 'Female', 89, '90/45', '0679190720'],
    ]
    data={
        'data': users
    }
    return render(request, 'reception/patients.html', data)

def payments(request, *args, **kwargs):
    users = [
        ['1-10-2021', 'Rajabu Mrisho', 25, 'Male', '0679190720', 4500],
        ['1-10-2021', 'Salehe Mrisho', 40, 'Male', '0679190720', 9000],
        ['1-10-2021', 'Jamila Mrisho', 40, 'Female', '0679190720', 10000],
    ]
    data={
        'data': users
    }
    return render(request, 'reception/payments.html', data)


def complaints(request, *args, **kwargs):
    return render(request, 'reception/complaints.html', {})
