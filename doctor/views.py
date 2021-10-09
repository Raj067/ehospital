from django.shortcuts import render

# Create your views here.
def dashboard(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data={
        'data': users
    }
    return render(request, 'doctor/home.html', data)


def admitted_patient(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'doctor/admitted-patient.html', data)


def outpatient_patient(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'doctor/outpatient-patient.html', data)


def report(request, *args, **kwargs):
    users = []
    data = {
        'data': users
    }
    return render(request, 'doctor/report.html', data)
