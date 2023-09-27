from django.db import models
from django.db.models import Model

PRIORIDADE = (
    (1, "Urgente"),
    (2, "Alta"),
    (3, "Media"),
    (4, "Baixa"),
    (5, "Irrisoria"),
)

class Usuario(Model):
    email = models.CharField("Email")
    data_cadastro = models.DateTimeField("Data de Cadastro")
    last_login   = models.DateTimeField("Ultimo Login")

class PessoaFisica(Model):
    cpf = models.BigIntegerField(primary_key=True)
    data_nascimento = models.DateField()
    primeiro_nome = models.CharField("Primeiro Nome")
    sobrenome = models.CharField("Sobrenome")

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

class Telefone(Model):
    telefone = models.CharField("Número de Telefone")
    ddd = models.IntegerField()
    pais = models.IntegerField()

class Endereco(Model):
    cep = models.CharField("CEP", max_length=9)

class Profissional(Model):
    registro_profissional = models.CharField("Registro Profissional")
    codigo_cbo = models.CharField("Especialização CBO")

class Instituicao(Model):
    nome = models.CharField("Nome da Instituição")
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False, blank=False)
    instituicao_gestora = models.OneToOneField("Instituicao", on_delete=models.SET_NULL, null=True, blank= False) 

class VinculoProfissional(Model):
    profissional = models.ForeignKey(Profissional)
    instituicao  = models.ForeignKey(Instituicao)
    is_active       = models.BooleanField("Vinculo Ativo?", default=True)

