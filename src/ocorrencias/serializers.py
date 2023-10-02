from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from rest_framework import serializers

from .models import *
from common.serializers import EnderecoSerializer
from common.models import *

class OcorrenciaSerializer(ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

class AtendimentoSerializer(ModelSerializer):
    endereco = EnderecoSerializer()
    ocorrencia = OcorrenciaSerializer(required=False)
    ocorrencia_id = PrimaryKeyRelatedField(queryset=Ocorrencia.objects.all(), required=False, write_only=True)

    class Meta:
        model = Atendimento
        fields = '__all__'

    def validate(self, data):
        ocorrencia = data.get('ocorrencia')
        ocorrencia_id = data.get('ocorrencia_id')

        if ocorrencia and ocorrencia_id:
            raise serializers.ValidationError("Você não pode fornecer dados para 'ocorrencia' e 'ocorrencia_id' ao mesmo tempo.")
        
        if not (ocorrencia or ocorrencia_id):
            raise serializers.ValidationError("Você deve fornecer dados para 'ocorrencia' ou 'ocorrencia_id'.")

        return data

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_data)

        ocorrencia_data = validated_data.pop('ocorrencia', None)
        ocorrencia_id   = validated_data.pop('ocorrencia_id', None)
        
        if ocorrencia_id:
            ocorrencia = ocorrencia_id
        else:
            ocorrencia = Ocorrencia.objects.create(**ocorrencia_data)
        
        operadores_data = validated_data.pop('operadores', [])

        atendimento = Atendimento.objects.create(endereco = endereco, ocorrencia = ocorrencia, **validated_data)
        
        atendimento.operadores.set(operadores_data)
        
        return atendimento 

class RelatorioSerializer(ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'
