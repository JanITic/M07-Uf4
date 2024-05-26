from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('create/', views.create_usuari, name='create_usuari'),
    path('update/<int:id>/', views.update_usuari, name='update_usuari'),
    path('delete/<int:id>/', views.delete_usuari, name='delete_usuari'),
]
