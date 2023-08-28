from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']  # Rôle sélectionné par l'utilisateur (étudiant, enseignant, administrateur)

        # Création d'un nouvel utilisateur
        user = User.objects.create_user(username=username, password=password)
        
        # Gérer les rôles en utilisant les groupes
        if role == 'student':
            student_group = Group.objects.get(name='Student')
            user.groups.add(student_group)
        elif role == 'teacher':
            teacher_group = Group.objects.get(name='Teacher')
            user.groups.add(teacher_group)
        elif role == 'admin':
            admin_group = Group.objects.get(name='Admin')
            user.groups.add(admin_group)
        
        user.save()

        return redirect('login')

    return render(request, 'registration/register.html')
