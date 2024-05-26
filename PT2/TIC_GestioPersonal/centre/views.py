from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuari, Rol
from .forms import UsuariForm, RolForm

def index(request):
    return render(request, 'index.html')

def students(request):
    students_data = Usuari.objects.filter(rol__nom='Estudiant')
    return render(request, 'student.html', {"data": students_data})

def teachers(request):
    teachers_data = Usuari.objects.filter(rol__nom='Professor')
    return render(request, 'teacher.html', {"data": teachers_data})

def create_usuari(request):
    if request.method == 'POST':
        form = UsuariForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuariForm()
    return render(request, 'form.html', {'form': form})

def update_usuari(request, id):
    usuari = get_object_or_404(Usuari, id=id)
    if request.method == 'POST':
        form = UsuariForm(request.POST, instance=usuari)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuariForm(instance=usuari)
    return render(request, 'form.html', {'form': form})

def delete_usuari(request, id):
    usuari = get_object_or_404(Usuari, id=id)
    if request.method == 'POST':
        usuari.delete()
        return redirect('index')
    return render(request, 'confirm_delete.html', {'object': usuari})
