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
    return render(request, 'nurse/home.html', data)


def all_schedule(request, *args, **kwargs):
    users = [
        ['1-10-2021', '9:00AM - 12:00AM', 'Rajabu Mrisho', 'Male', 'Consultation', 'Normal'],
        ['2-10-2021', '9:00AM - 12:00AM', 'Salehe Mrisho', 'Male', 'Imaging', 'stable'],
        ['3-10-2021', '9:00AM - 12:00AM', 'Jamila Mrisho', 'Female', 'Imaging', 'unstable'],
    ]
    data={
        'data': users
    }
    return render(request, 'nurse/all_schedule.html', data)


def today_schedule(request, *args, **kwargs):
    users = [
        ['1-10-2021', '9:00AM - 12:00AM', 'Rajabu Mrisho', 'Male', 'Consultation', 'Normal'],
        ['2-10-2021', '9:00AM - 12:00AM', 'Salehe Mrisho', 'Male', 'Imaging', 'stable'],
    ]
    data = {
        'data': users
    }
    return render(request, 'nurse/today_schedule.html', data)


def add_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'nurse/add_schedule.html', data)


def theater_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'nurse/theater_schedule.html', data)


def add_theater_schedule(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'nurse/add_theater_schedule.html', data)


def medication_requests(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'nurse/medication_requests.html', data)


def medication_completed(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'nurse/medication_completed.html', data)


def report(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'nurse/report.html', data)


def complaints(request, *args, **kwargs):
    users = [
        ['I0001', 'Rajabu Mrisho', 'Male', 43, 'Normal', '23/56'],
        ['I0002', 'Salehe Mrisho', 'Male', 67, 'stable', '90/45'],
        ['I0003', 'Jamila Mrisho', 'Female', 89, 'unstable', '90/45'],
    ]
    data = {
        'data': users
    }
    return render(request, 'nurse/complaints.html', data)
