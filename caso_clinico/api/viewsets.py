from rest_framework.viewsets import ModelViewSet
from caso_clinico.models import CasoClinico, CasoComentario
from caso_clinico.api.serializer import CasoClinicoSerializer, CasoComentarioSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CasoClinicoViewSet(ModelViewSet):
    queryset = CasoClinico.objects.all()
    serializer_class = CasoClinicoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']


class CasoComentarioViewSet(ModelViewSet):
    queryset = CasoComentario.objects.all()
    serializer_class = CasoComentarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['caso', 'author']




