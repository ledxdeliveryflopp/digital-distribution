from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework.fields import CharField


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


class RegisterSerializer(ModelSerializer):
    """Сериалайзер регистрации"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'avatar', 'region']
