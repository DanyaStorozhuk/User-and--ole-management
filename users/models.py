from django.db import models

# Create your models here.

class Rol(models.Model):
    name_rol = models.CharField(max_length=50)


class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"Name:{self.name}, age:{self.age}, email:{self.email}, rol:{self.rol.name_rol}"
