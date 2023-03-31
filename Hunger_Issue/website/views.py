from django.shortcuts import render
from .forms import MyModelForm


def index(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            # Do something after saving the form
    else:
        form = MyModelForm()
    return render(request, 'index.html', {'form': form})


def userform_view(request):
    return render(request, 'userform.html')


def afterlocation_view(request):
    return render(request, 'afterlocation.html')


def about_view(request):
    return render(request, 'about.html')

def login_view(request):
    return render(request, 'login.html')

def map_view(request):
    return render(request, 'map.html')

def home_view(request):
    return render(request, 'index.html')

def donate_view(request):
    return render(request, 'fooddonate.html')