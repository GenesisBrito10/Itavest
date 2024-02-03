# controle_bordado/urls.py

from django.contrib import admin
from django.urls import path,include
from bordados import views

urlpatterns = [
    path('', admin.site.urls),
    path('bordados/', views.lista_bordados, name='lista_bordados'),
    path('bordados/novo/', views.novo_bordado, name='novo_bordado'),
    path('bordados/editar/<int:bordado_id>/', views.editar_status, name='editar_status'),
    path('api/', include('bordados.urls')),

]
