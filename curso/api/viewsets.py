from rest_framework.viewsets import ModelViewSet
from curso.models import Curso, CursoComentario
from curso.api.serializer import CursoSerializer, CursoComentarioSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']


class CursoComentarioViewSet(ModelViewSet):
    queryset = CursoComentario.objects.all()
    serializer_class = CursoComentarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['curso', 'author']




