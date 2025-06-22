import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_role_managment.settings")





django.setup()
from users.models import Rol, User

#Rol.objects.create(name_rol = 'admin')
#Rol.objects.create(name_rol = 'superuser')
#Rol.objects.create(name_rol = 'user_defolt')

#User.objects.create(name = "Ivan", age = 19, email = "Ivan@gmail.com", rol = Rol.objects.get(name_rol = 'admin'))
#User.objects.create(name = "Petro", age = 17, email = "Petro@gmail.com", rol = Rol.objects.get(name_rol = 'superuser'))
#User.objects.create(name = "Vasia", age = 13, email = "Vasia@gmail.com", rol = Rol.objects.get(name_rol = 'user_defolt'))


user_1 = User.objects.get(name = "Ivan")
print(user_1)