from django.forms import ModelForm
from .models import Task, Profile


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["biography"]
