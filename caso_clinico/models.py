from django.contrib.auth.models import User
from django.db import models


class CasoClinico(models.Model):
    nome = models.CharField('NOME', max_length=50)
    descricao = models.CharField('DESCRIÇÃO', max_length=500)
    author = models.CharField('Author', max_length=50)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    status = models.BooleanField('Status', default=False)
    def __str__(self):
        return self.nome


class CasoComentario(models.Model):
    caso = models.ForeignKey(CasoClinico, on_delete=models.CASCADE)
    nome = models.CharField('NOME', max_length=50)
    descricao = models.CharField('DESCRIÇÃO', max_length=500)
    author = models.CharField('Author', max_length=50)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    status = models.BooleanField('Status', default=False)    

    def __str__(self):
        return self.nome
