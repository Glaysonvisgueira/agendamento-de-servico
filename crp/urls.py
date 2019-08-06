from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from crp import views

urlpatterns = [    
    path('cadastrar-crp/',views.cadastrar_crp, name="cadastrar_crp"),
    path('relatorio-de-crps-pendentes/',views.relatorio_de_crps_pendentes, name="relatorio_de_crps_pendentes"),
    url(r'^editar-chegada-peca/(?P<pk>\d+)/edit/$', views.editar_chegada_peca, name="editar_chegada_peca"),
    url(r'^envio-setor-entrega/(?P<pk>\d+)/edit/$', views.envio_setor_entrega, name="envio_setor_entrega"),
     url(r'^data-recebimento-crp-entrega/(?P<pk>\d+)/edit/$', views.data_recebimento_entrega, name="data_recebimento_entrega"),
    url(r'^data-conclusao-crp/(?P<pk>\d+)/edit/$', views.data_conclusao_crp, name="data_conclusao_crp"),
]