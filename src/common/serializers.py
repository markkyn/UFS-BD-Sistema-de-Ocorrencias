from rest_framework.serializers import ModelSerializer
from .models import *

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'senha']

class PessoaFisicaSerializer(ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = PessoaFisica
        fields = '__all__'

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create(**usuario_data)
        pessoa_fisica = PessoaFisica.objects.create(usuario = usuario, **validated_data)
        return pessoa_fisica 

class ProfissionalSerializer(ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

class InstituicaoSerializer(ModelSerializer):
    class Meta:
        model = Instituicao
        fields = '__all__'

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'