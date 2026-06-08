from django.db import models
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    plano = models.CharField(max_length=50)

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return self.plano