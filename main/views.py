from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Artur',
        'values': ["some", "hello", "12345"],
        "obj": {
            'car': 'bmw',
            'age': '19',
            'name': "Arseny"
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
