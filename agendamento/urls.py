"""agendamento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.conf.urls import url


urlpatterns = [
	path('',views.home, name="home"),
    path('crp/', include('crp.urls')),
    path('admin/', admin.site.urls),
    path('login/',views.login, name="login"),
    path('cadastrar-agendamento/',views.agendar, name="agendar"),
    path('listar-agendamentos/',views.listarAgendamentos, name="listarAgendamentos"),    
    path('events/',views.PostList, name="paginator"),
    url(r'^editar-agendamento/(?P<pk>\d+)/edit/$', views.editarAgendamento, name='editarAgendamento'),
]
