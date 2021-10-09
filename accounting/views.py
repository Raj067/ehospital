from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data={
        'data': users
    }
    return render(request, 'accounting/home.html', data)

def complaints(request, *args, **kwargs):
    return render(request, 'accounting/complaints.html', {})


def admitted_patient(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'accounting/admitted-patient.html', data)


def outpatient_patient(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'accounting/outpatient-patient.html', data)


def report(request, *args, **kwargs):
    users = []
    data = {
        'data': users
    }
    return render(request, 'accounting/report.html', data)


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
    return render(request, 'accounting/all_schedule.html', data)


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
    return render(request, 'accounting/today_schedule.html', data)


def add_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'accounting/add_schedule.html', data)


def theater_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'accounting/theater_schedule.html', data)


def add_theater_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'accounting/add_theater_schedule.html', data)


def invoice(request, *args, **kwargs):
    return render(request, 'accounting/invoice.html', {})


def new_invoice(request, *args, **kwargs):
    return render(request, 'accounting/new-invoice.html', {})


def price(request, *args, **kwargs):
    return render(request, 'accounting/price.html', {})


def price_profile(request, *args, **kwargs):
    return render(request, 'accounting/price-profile.html', {})
