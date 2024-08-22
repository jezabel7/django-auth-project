from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Utilizamos el modelo integrado User


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    print(request)
    form = {"form": UserCreationForm}
    if request.method == "GET":
        return render(request, "signup.html", form)
    else:
        # creación de usuario
        user = User.objects.create_user(
            username=request.POST["username"], password=request.POST["password1"]
        )
        user.save()
        print(request.POST)
        return redirect("home")


def login(request):
    return render(request, "login.html")


def home(request):
    print("home")
    users = User.objects.all()
    print(users)
    return render(request, "home.html")
