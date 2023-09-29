from rest_framework import viewsets

from .models import *
from .serializers import *

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PessoaFisicaViewSet(viewsets.ModelViewSet):
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer

