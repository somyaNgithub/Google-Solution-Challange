from django.shortcuts import render
import pyrebase
from .forms import MyModelForm
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from django.contrib.auth.models import User


config = {
  "apiKey": "AIzaSyDJS6zb6mWXtZM__vtpncfRfjrmgtAzaqc",
  "authDomain": "hackathonjaipur-c0ee0.firebaseapp.com",
  "projectId": "hackathonjaipur-c0ee0",
  "storageBucket": "hackathonjaipur-c0ee0.appspot.com",
  "messagingSenderId": "154178091966",
  "appId": "1:154178091966:web:a56dd0453f60b9d75cd7ef",
  "measurementId": "G-S9116ES65H"
}

cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            # User is authenticated
        except auth.InvalidEmailError:
            # Handle invalid email error
        except auth.InvalidPasswordError:
            # Handle invalid password error
        except auth.UserNotFoundError:
            # Handle user not found error


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            # User is authenticated
            uid = user['localId']
            # Check if the user exists in Django's database
            django_user, created = User.objects.get_or_create(username=uid)
            django_user.set_password(password)
            django_user.save()
            # Log in the user using Django's authentication system
            auth_login(request, django_user)
        except auth.InvalidEmailError:
            # Handle invalid email error
        except auth.InvalidPasswordError:
            # Handle invalid password error
        except auth.UserNotFoundError:
            # Handle user not found error




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