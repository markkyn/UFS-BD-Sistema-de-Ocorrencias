from rest_framework.serializers import ModelSerializer

from .models import *
from common.serializers import EnderecoSerializer

class OcorrenciaSerializer(ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

class AtendimentoSerializer(ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = Atendimento
        fields = '__all__'

class RelatorioSerializer(ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'