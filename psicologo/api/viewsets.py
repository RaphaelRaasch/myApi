from rest_framework.viewsets import ModelViewSet
from psicologo.models import Psicologo, Formacao
from psicologo.api.serializer import PsicologoSerializer, FormacaoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PsicologoViewSet(ModelViewSet):
    queryset = Psicologo.objects.all()
    serializer_class = PsicologoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']


class FormacaoViewSet(ModelViewSet):
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['psicologo']



