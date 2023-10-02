from rest_framework.serializers import ModelSerializer

from .models import *
from common.serializers import EnderecoSerializer

class OcorrenciaSerializer(ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

class AtendimentoSerializer(ModelSerializer):
    endereco = EnderecoSerializer()
    ocorrencia = OcorrenciaSerializer()

    class Meta:
        model = Atendimento
        fields = '__all__'

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_data)

        ocorrencia_data = validated_data.pop('ocorrencia')
        ocorrencia = Ocorrencia.objects.create(**ocorrencia_data)
        
        atendimento = Atendimento.objects.create(endereco = endereco, ocorrencia = ocorrencia, **validated_data)
        return atendimento 

class RelatorioSerializer(ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'
