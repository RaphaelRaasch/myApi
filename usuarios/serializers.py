
from rest_framework.serializers import ModelSerializer
from usuarios.models import CustomUsuario

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUsuario
        fields = ('id','first_name', 'last_name', 'email')