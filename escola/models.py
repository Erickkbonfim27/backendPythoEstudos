from django.db import models
from django.db.models import CASCADE
from django.core.validators import MinLengthValidator

class Estudante(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(blank=False, max_length=50)
    cpf = models.CharField(blank= False, max_length=11, unique=True)
    data_nascimento = models.DateField()
    numero_celular = models.CharField(max_length=14)


    def __str__(self):
        return self.nome



class Curso(models.Model):
    NIVEL = {
        ("B", "Basico"),
        ("i", "Intermediario"),
        ("A", "Avancado"),
    }

    codigo = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(3)] ) #esquema pra colocar validações personalizadas e as do django também, legal isso aqui, além daqui da pra faer validações pelo serializer
    descricao = models.CharField(blank=False, max_length=255)
    nivel = models.CharField(max_length=1, blank=False, null=False, choices = NIVEL, default="B")

    def __str__(self):
        return self.codigo


class Matricula(models.Model):
    PERIODO = (
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Noturno"),
    )
    estudante = models.ForeignKey(Estudante, on_delete=CASCADE)
    curso = models.ForeignKey(Curso, on_delete=CASCADE)
    periodo = models.CharField(max_length=1, blank=False, null=False, choices=PERIODO, default="M")
