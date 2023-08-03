from rest_framework.serializers import ModelSerializer
from .models import User


class AllUserSerializer(ModelSerializer):
    """Сериалайзер всех пользователей"""

    class Meta:
        model = User
        fields = ['username', 'Region', 'avatar']


class UserSerializer(ModelSerializer):
    """Сериалайзер отдельного пользователя"""

    class Meta:
        model = User
        fields = '__all__'
