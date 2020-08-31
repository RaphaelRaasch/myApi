from rest_framework.serializers import ModelSerializer
from curso.models import Curso, CursoComentario


class CursoSerializer(ModelSerializer):

    class Meta:
        model = Curso
        fields = ['id', 'nome', 'descricao', 'author', 'qtd_horas', 'local', 'data', 'hora', 'status', 'created_at', 'modified_at']


class CursoComentarioSerializer(ModelSerializer):

    class Meta:
        model = CursoComentario
        fields = ['id', 'curso', 'nome', 'descricao', 'author', 'status', 'created_at', 'modified_at']
