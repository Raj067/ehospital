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

def complaints(request, *args, **kwargs):
    return render(request, 'doctor/compaints.html', {})


def medication_request(request, *args, **kwargs):
    return render(request, 'doctor/medication-request.html', {})


def medication_completed(request, *args, **kwargs):
    return render(request, 'doctor/medication-completed.html', {})


def medication_new(request, *args, **kwargs):
    return render(request, 'doctor/medication-new.html', {})


def imaging_request(request, *args, **kwargs):
    return render(request, 'doctor/imaging-request.html', {})


def imaging_completed(request, *args, **kwargs):
    return render(request, 'doctor/imaging-completed.html', {})


def all_schedule(request, *args, **kwargs):
    users = [
        ['1-10-2021', '9:00AM - 12:00AM', 'Rajabu Mrisho',
            'Male', 'Consultation', 'Normal'],
        ['2-10-2021', '9:00AM - 12:00AM',
            'Salehe Mrisho', 'Male', 'Imaging', 'stable'],
        ['3-10-2021', '9:00AM - 12:00AM', 'Jamila Mrisho',
            'Female', 'Imaging', 'unstable'],
    ]
    data = {
        'data': users
    }
    return render(request, 'doctor/all_schedule.html', data)


def today_schedule(request, *args, **kwargs):
    users = [
        ['1-10-2021', '9:00AM - 12:00AM', 'Rajabu Mrisho',
            'Male', 'Consultation', 'Normal'],
        ['2-10-2021', '9:00AM - 12:00AM',
            'Salehe Mrisho', 'Male', 'Imaging', 'stable'],
    ]
    data = {
        'data': users
    }
    return render(request, 'doctor/today_schedule.html', data)


def add_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'doctor/add_schedule.html', data)


def theater_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'doctor/theater_schedule.html', data)


def add_theater_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'doctor/add_theater_schedule.html', data)
