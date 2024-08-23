from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Utilizamos el modelo integrado User
from django.contrib.auth import login


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "index.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    print(request)
    print(request.method)

    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        try:
            if request.POST["password1"] == request.POST["password2"]:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                print(request.POST)
                return redirect("home")
            else:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
                )
        except:
            return render(
                request,
                "signup.html",
                {"form": UserCreationForm, "error": "El usuario ya existe"},
            )


def session(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "login.html")


def delete_session(request):
    if request.user.is_authenticated:
        return HttpResponse("cerrar sesión")
    return redirect("index")


def home(request):
    if request.user.is_authenticated:
        print("home")
        users = User.objects.all()
        print(users)
        return render(request, "home.html")
    return redirect("index")
