from django.contrib.auth.models import User
from django.db import models


class Curso(models.Model):
    nome = models.CharField('NOME', max_length=50)
    descricao = models.CharField('DESCRIÇÃO', max_length=150)
    author = models.CharField('Author', max_length=50)
    qtd_horas = models.CharField('Quantidade de Horas', max_length=5)
    local = models.CharField('LOCAL', max_length=155)
    data = models.CharField('Data', max_length=5)
    hora = models.CharField('Hora', max_length=5)
    status = models.BooleanField('STATUS', default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
   
    def __str__(self):
        return self.nome


class CursoComentario(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome = models.CharField('NOME', max_length=50)
    descricao = models.CharField('DESCRIÇÃO', max_length=150)
    author = models.CharField('Author', max_length=50)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    status = models.BooleanField('Status', default=False)

    def __str__(self):
        return self.nome
