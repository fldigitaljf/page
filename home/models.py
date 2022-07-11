
from django.db import models



class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.IntegerField(max_length=11)
    assunto = models.CharField(max_length=255)
    texto = models.CharField(max_length=800)
# Create your models here.

class Inscribe(models.Model):
    mail_inscrito = models.CharField(max_length=255)
