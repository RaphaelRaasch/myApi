from elis.settings import AUTH_USER_MODEL
from django.db import models


class Psicologo(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    crp = models.IntegerField('CRP')

    def __str__(self):
        return f'{self.crp}'



class Formacao(models.Model):
    TITULO_CHOICES = (
        ('GRADUACAO', 'GRADUACAO'),
        ('MESTRADO', 'MESTRADO'),
        ('DOUTORADO', 'DOUTORADO'),
    )
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    nome = models.CharField('Nome do curso', max_length=155)
    titulo = models.CharField('TITULO', max_length=10, choices=TITULO_CHOICES)
    instituicao = models.CharField('INSTITUICAO', max_length=155)
    concluido = models.BooleanField('CONCLUIDO')
    data_conclusao = models.CharField('Data', max_length=50)

    def __str__(self):
        return self.titulo






