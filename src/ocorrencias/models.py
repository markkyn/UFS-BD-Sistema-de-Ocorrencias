from django.db import models
from django.db.models import Model

from common.models import Solicitante, Operacional, Endereco


PRIORIDADE = (
    (1,"Urgente"),
    (2, "Alta"),
    (3, "Media"),
    (4, "Baixa"),
    (5,"Irrisorio"),
)

class Ocorrencia(Model):
    datahora_criacao = models.DateTimeField("Data de Criação",auto_now=True)
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    prioridade = models.IntegerField(default=3, choices=PRIORIDADE)
    observações = models.TextField()

class Atendimento(Model):
    datahora_atendimento = models.DateTimeField("Data do Atendimento")
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    ocorrencia = models.Foreignkey(Ocorrencia, on_delete=models.CASCADE)
    operadores = models.ManyToManyField(Operacional)

class Relatorio(Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)
    texto = models.TextField()
