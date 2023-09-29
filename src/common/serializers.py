from rest_framework.serializers import ModelSerializer
from .models import *

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PessoaFisicaSerializer(ModelSerializer):
    class Meta:
        model = PessoaFisica
        fields = '__all__'

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