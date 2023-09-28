from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator, MaxValueValidator, 


PRIORIDADE = (
    (1, "Urgente"),
    (2, "Alta"),
    (3, "Media"),
    (4, "Baixa"),
    (5, "Irrisorio"),
)

class Usuario(Model):
    email = models.CharField("Email")
    data_cadastro = models.DateTimeField("Data de Cadastro")
    last_login   = models.DateTimeField("Ultimo Login")

class Telefone(Model):
    numero = models.IntegerField("Número de Telefone", validators=[MinValueValidator(970_000_000), MaxValueValidator(999_999_999)])
    ddd = models.IntegerField("DDD", validators=[MinValueValidator(11), MaxValueValidator(99)])
    pais = models.IntegerField("País de Origem", validators=[MinValueValidator(11), MaxValueValidator(99)] )
    pessoa = models.ForeignKey("PessoaFisica", on_delete=models.CASCADE)


class PessoaFisica(Model):
    cpf = models.BigIntegerField("CPF", primary_key=True, validators=[MinValueValidator(10_000_000_000), MaxValueValidator(99_999_999_999)])
    data_nascimento = models.DateField("Data de Nascimento")
    primeiro_nome = models.CharField("Primeiro Nome")
    sobrenome = models.CharField("Sobrenome")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    @property
    def telefones(self):
        return Telefone.objects.filter(pessoa = self)

    @telefones.setter
    def telefones(self, novo_telefone):
        self.telefones = Telefone.objects.create(
            pessoa = self,
            pais = novo_telefone.pais,
            ddd = novo_telefone.ddd, 
            numero = novo_telefone.numero,
        )

class Endereco(Model):
    cep = models.CharField("CEP", max_length=9)
    bairro = models.CharField("Bairro", max_length=45)
    rua = models.CharField("Nome da Rua", max_length=45)

class Profissional(Model):
    registro_profissional = models.CharField("Registro Profissional")
    codigo_cbo = models.CharField("Especialização CBO")

class Instituicao(Model):
    nome = models.CharField("Nome da Instituição")
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False, blank=False)
    instituicao_gestora = models.OneToOneField("Instituicao", on_delete=models.SET_NULL, null=True, blank= False) 

class VinculoProfissional(Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    instituicao  = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    is_active    = models.BooleanField("Vinculo Ativo?", default=True)

