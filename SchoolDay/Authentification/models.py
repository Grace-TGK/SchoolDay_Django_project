from django.db import models
from django.apps import AppConfig
from django.contrib.auth.models import Group

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Authentification'

    def ready(self):
        # Créer les groupes s'ils n'existent pas
        student_group, _ = Group.objects.get_or_create(name='Student')
        teacher_group, _ = Group.objects.get_or_create(name='Teacher')
        admin_group, _ = Group.objects.get_or_create(name='Admin')

