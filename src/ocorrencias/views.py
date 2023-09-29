from rest_framework import viewsets

from .models import *
from .serializers import *

class OcorrenciasViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer

class AtendimentoViewSet(viewsets.ModelViewSet):
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer