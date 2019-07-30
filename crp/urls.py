from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from crp import views

urlpatterns = [    
    path('cadastrar-crp/',views.cadastrar_crp, name="cadastrar_crp"),
    path('relatorio-de-crps-pendentes/',views.relatorio_de_crps_pendentes, name="relatorio_de_crps_pendentes"),

]