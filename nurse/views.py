from django.shortcuts import render

# Create your views here.
def dashboard(request, *args, **kwargs):
    users = [
        ['Rajabu Mrisho', 25, 'Male', 49, '23/56', '0679190720'],
        ['Salehe Mrisho', 40, 'Male', 89, '90/45', '0679190720'],
        ['Jamila Mrisho', 40, 'Female', 89, '90/45', '0679190720'],
    ]
    data={
        'data': users
    }
    return render(request, 'nurse/home.html', data)