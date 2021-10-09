from django.shortcuts import render

# Create your views here.


def dashboard(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'administrator/home.html', data)


def admitted_patient(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'administrator/admitted-patient.html', data)


def outpatient_patient(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'administrator/outpatient-patient.html', data)


def report(request, *args, **kwargs):
    users = []
    data = {
        'data': users
    }
    return render(request, 'administrator/report.html', data)


def complaints(request, *args, **kwargs):
    return render(request, 'administrator/complaints.html', {})


def medication_request(request, *args, **kwargs):
    return render(request, 'administrator/medication-request.html', {})


def medication_completed(request, *args, **kwargs):
    return render(request, 'administrator/medication-completed.html', {})


def medication_new(request, *args, **kwargs):
    return render(request, 'administrator/medication-new.html', {})


def imaging_request(request, *args, **kwargs):
    return render(request, 'administrator/imaging-request.html', {})


def imaging_completed(request, *args, **kwargs):
    return render(request, 'administrator/imaging-completed.html', {})


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
    return render(request, 'administrator/all_schedule.html', data)


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
    return render(request, 'administrator/today_schedule.html', data)


def add_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'administrator/add_schedule.html', data)


def theater_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'administrator/theater_schedule.html', data)


def add_theater_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'administrator/add_theater_schedule.html', data)


def lab_request(request, *args, **kwargs):
    return render(request, 'administrator/lab-request.html', {})


def lab_completed(request, *args, **kwargs):
    return render(request, 'administrator/lab-completed.html', {})


def lab_new(request, *args, **kwargs):
    return render(request, 'administrator/lab-new.html', {})


def invoice(request, *args, **kwargs):
    return render(request, 'administrator/invoice.html', {})


def new_invoice(request, *args, **kwargs):
    return render(request, 'administrator/new-invoice.html', {})


def price(request, *args, **kwargs):
    return render(request, 'administrator/price.html', {})


def price_profile(request, *args, **kwargs):
    return render(request, 'administrator/price-profile.html', {})


def current_incident(request, *args, **kwargs):
    return render(request, 'administrator/current-incident.html', {})


def new_incident(request, *args, **kwargs):
    return render(request, 'administrator/new-incident.html', {})


def history_incident(request, *args, **kwargs):
    return render(request, 'administrator/history-incident.html', {})


def report_incident(request, *args, **kwargs):
    return render(request, 'administrator/report-incident.html', {})
