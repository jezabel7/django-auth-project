from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  # Utilizamos el modelo integrado User
from django.contrib.auth import login, authenticate, logout
from .models import Task, Profile, Comment
from .forms import TaskForm, ProfileForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "index.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "GET":
        return render(request, "signup.html")
    else:
        print(request.POST)
        try:
            if request.POST["password1"] == request.POST["password2"]:

                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()

                profile = Profile.objects.create(user=user)
                profile.save()

                login(request, user)
                return redirect("home")
            else:
                return render(
                    request,
                    "signup.html",
                    {"error": "Las contraseñas no coinciden"},
                )
        except:
            return render(
                request,
                "signup.html",
                {"error": "El usuario ya existe"},
            )


def session(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm,
                    "error": "El username o password es incorrecto",
                },
            )
        login(request, user)
        return redirect("home")


def delete_session(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")

    return redirect("index")


def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all()  # Obtiene todas las tareas de la BD
        return render(request, "home.html", {"tasks": tasks})
    return redirect("index")


def create_task(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "create_task.html", {"form": TaskForm})
        else:
            try:
                print(request.POST)
                form = TaskForm(
                    request.POST
                )  # Crear el formulario con los datos enviados
                if form.is_valid():
                    nuevo_task = form.save(
                        commit=False
                    )  # Obtener los datos de ese form
                    nuevo_task.user = request.user
                    nuevo_task.save()
                    return redirect("home")
            except:
                return render(
                    request,
                    "create_task.html",
                    {"form": TaskForm, "error": "No se pudo crear la tarea"},
                )

    redirect("login")


def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    tasks = Task.objects.filter(user=profile.user)

    return render(request, "profile.html", {"profile": profile, "tasks": tasks})


def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request._files, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
        return render(request, "edit_profile.html", {"form": form})


def like_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.user in task.liked_by.all():
        task.liked_by.remove(request.user)
        liked = False
    else:
        task.liked_by.add(request.user)
        liked = True

    return JsonResponse({"liked": liked, "total_likes": task.total_likes()})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.task = task
            new_comment.user = request.user
            new_comment.save()
            return redirect("task_detail", task_id=task.id)
    else:
        form = CommentForm()

    return render(
        request, "task_detail.html", {"task": task, "comments": comments, "form": form}
    )


def add_comment(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.task = task
            new_comment.user = request.user
            new_comment.save()
    return redirect("home")


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "GET":
        form = CommentForm(instance=comment)
        return render(
            request, "edit_comment_form.html", {"form": form, "comment": comment}
        )
    elif request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return JsonResponse(
                {"success": True, "content": comment.content}
            )  # Enviar contenido actualizado
        return JsonResponse({"success": False, "errors": form.errors})
    if form.is_valid():
        comment = form.save()
