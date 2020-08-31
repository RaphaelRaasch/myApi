
from rest_framework.viewsets import ModelViewSet
from usuarios.models import CustomUsuario
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = CustomUsuario.objects.all()
    serializer_class = UserSerializer