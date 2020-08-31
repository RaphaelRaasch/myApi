from rest_framework.serializers import ModelSerializer
from psicologo.models import Psicologo, Formacao


class FormacaoSerializer(ModelSerializer):

    class Meta:
        model = Formacao
        fields = ['id','psicologo','nome', 'titulo', 'instituicao', 'concluido','data_conclusao']


class PsicologoSerializer(ModelSerializer):

    class Meta:
        model = Psicologo
        fields = 'id', 'user', 'crp',
