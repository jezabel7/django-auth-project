from django.db import models
from django.contrib.auth.models import User  # Django ya lo tiene implementado


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    datecompleted = models.DateTimeField(null=True)
    # relacionamos con el usuario | si en caso el usuario se borra, pues se borran sus tareas
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
