from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import *

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'senha']

class PessoaFisicaSerializer(ModelSerializer):
    usuario = UsuarioSerializer(required=False)
    usuario_id = PrimaryKeyRelatedField(queryset=Usuario.objects.all(), required=False, write_only=True)

    class Meta:
        model = PessoaFisica
        fields = '__all__'

    def validate(self, data):
        usuario = data.get("usuario")
        usuario_id = data.get("usuario_id")

        if usuario and usuario_id:
            raise serializers.ValidationError("Você não pode fornecer dados para 'usuario' e 'usuario_id' ao mesmo tempo.")

        if not (usuario or usuario_id):
            raise serializers.ValidationError("Você deve fornecer dados para 'usuario' ou 'usuario_id'.")

        return data

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario', None)
        usuario_id = validated_data.pop('usuario_id', None)

        if usuario_id:
            usuario = usuario_id
        else:
            usuario = Usuario.objects.create(**usuario_data)

        pessoa_fisica = PessoaFisica.objects.create(usuario = usuario, **validated_data)
        return pessoa_fisica 

class ProfissionalSerializer(ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

class SolicitanteSerializer(ModelSerializer):
    profissional = ProfissionalSerializer(required=False)
    profissional_id = PrimaryKeyRelatedField(queryset=Profissional.objects.all(), required=False, write_only=True)
    class Meta:
        model = Solicitante
        fields = '__all__'

    def validate(self, data):
        profissional = data.get('profissional')
        profissional_id = data.get('profissional_id')

        if profissional and profissional_id:
            raise serializers.ValidationError("Você não pode fornecer dados para 'profissional' e 'profissional_id' ao mesmo tempo.")

        if not (profissional or profissional_id):
            raise serializers.ValidationError("Você deve fornecer dados para 'profissional' ou 'profissional_id'.")

        return data
    
    def create(self, validated_data):
        profissional_data = validated_data.pop('profissional', None)
        profissional_id   = validated_data.pop('profissional_id', None)

        if profissional_id:
            profissional = profissional_id
        else:
            profissional = Profissional.objects.create(**profissional_data)

        solicitante = Solicitante.objects.create(profissional = profissional, **validated_data)
        
        return solicitante

class OperacionalSerializer(ModelSerializer):
    profissional = ProfissionalSerializer(required=False)
    profissional_id = PrimaryKeyRelatedField(queryset=Profissional.objects.all(), required=False, write_only=True)

    class Meta:
        model = Operacional
        fields = '__all__'

    def validate(self, data):
        profissional = data.get('profissional')
        profissional_id = data.get('profissional_id')

        if profissional and profissional_id:
            raise serializers.ValidationError("Você não pode fornecer dados para 'profissional' e 'profissional_id' ao mesmo tempo.")

        if not (profissional or profissional_id):
            raise serializers.ValidationError("Você deve fornecer dados para 'profissional' ou 'profissional_id'.")

        return data

    def create(self, validated_data):
        profissional_data = validated_data.pop('profissional', None)
        profissional_id   = validated_data.pop('profissional_id', None)

        if profissional_id:
            profissional = profissional_id
        else:
            profissional = Profissional.objects.create(**profissional_data)

        operacional = Operacional.objects.create(profissional = profissional, **validated_data)
        
        return operacional

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
class InstituicaoSerializer(ModelSerializer):
    endereco = EnderecoSerializer()
    
    class Meta:
        model = Instituicao
        fields = '__all__'

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_data)

        instituicao = Instituicao.objects.create(endereco=endereco,**validated_data)
        return instituicao