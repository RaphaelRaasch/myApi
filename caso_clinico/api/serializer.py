from rest_framework.serializers import ModelSerializer
from caso_clinico.models import CasoClinico, CasoComentario


class CasoClinicoSerializer(ModelSerializer):

    class Meta:
        model = CasoClinico
        fields = ['id', 'nome', 'descricao', 'author', 'created_at', 'modified_at', 'status']


class CasoComentarioSerializer(ModelSerializer):

    class Meta:
        model = CasoComentario
        fields = ['id', 'caso', 'nome', 'descricao', 'author', 'created_at', 'modified_at', 'status']
