from django.db import models

# Create your models here.


class Teste(models.Model):
    name = models.TextField(unique=True)


class User(models.Model):
    name = models.CharField(unique=True, max_length=255)


class Vendedor(models.Model):
    name = models.CharField(max_length=255),
    cpf = models.IntegerField(unique=True)
