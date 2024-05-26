from django.contrib import admin
from django.urls import path, include
from centre import views  # Asegúrate de importar las vistas de la aplicación centre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('centre/', include('centre.urls')),
    path('', views.index, name='index'),  # Añade esta línea para la URL raíz
]
