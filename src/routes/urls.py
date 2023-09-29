"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from common.views import *
from ocorrencias.views import *


# Definições de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Sistema de Ocorrências",
        default_version='v1',
        description="Projeto idealizado por Marcos Gabriel e Vinícius Peroba para discipina de Banco de Dados, Turma 1, do período 2023.1 da Universidade Federal de Sergipe",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Comum
router = DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('pessoas_fisicas', PessoaFisicaViewSet)
router.register('profissionais', ProfissionalViewSet)
router.register('instituicoes', InstituicaoViewSet)

# Ocorrencias
router.register('ocorrencias', OcorrenciasViewSet)
router.register('atendimentos', AtendimentoViewSet)
router.register('relatorios', RelatorioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls), name="router"),
]
