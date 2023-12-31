from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.hashers import make_password

class Usuario(Model):
    email = models.CharField("Email", max_length=255, unique = True)
    senha = models.CharField("Senha", max_length=128, default=None)
    data_cadastro = models.DateTimeField("Data de Cadastro", auto_now=True)
    last_login    = models.DateTimeField("Ultimo Login", null=True)

    def save(self, *args, **kwargs):
        if self.pk:
            orig = Usuario.objects.get(pk=self.pk)
            if orig.senha != self.senha:
                self.senha = make_password(self.senha)
        else:
            self.senha = make_password(self.senha)

        super(Usuario, self).save(*args, **kwargs)

class Telefone(Model):
    numero = models.IntegerField("Número de Telefone", validators=[MinValueValidator(970_000_000), MaxValueValidator(999_999_999)])
    ddd = models.IntegerField("DDD", validators=[MinValueValidator(11), MaxValueValidator(99)])
    pais = models.IntegerField("País de Origem", validators=[MinValueValidator(11), MaxValueValidator(99)] )
    pessoa = models.ForeignKey("PessoaFisica", on_delete=models.CASCADE)

class PessoaFisica(Model):
    cpf = models.BigIntegerField("CPF", primary_key=True, validators=[MinValueValidator(1_000_000_000), MaxValueValidator(99_999_999_999)])
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
    bairro = models.CharField("Bairro", max_length=45, null=False)
    rua = models.CharField("Nome da Rua", max_length=45)

class Instituicao(Model):
    nome = models.CharField("Nome da Instituição")
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False, blank=False)
    instituicao_gestora = models.OneToOneField("Instituicao", on_delete=models.SET_NULL, null=True, blank= False) 

class Profissional(Model):
    registro_profissional = models.CharField("Registro Profissional")
    codigo_cbo = models.CharField("Especialização CBO")
    pessoa_cpf = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE)

class VinculoProfissional(Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    instituicao  = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    is_active    = models.BooleanField("Vinculo Ativo?", default=True)

# Especializações de Profissional
class Solicitante(Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)

class Operacional(Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)