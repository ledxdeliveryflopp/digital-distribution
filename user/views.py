from rest_framework import generics, filters
from .models import User
from .serializers import AllUserSerializer, UserSerializer


class AllUserApiView(generics.ListAPIView):
    """Представление всех пользователй"""
    queryset = User.objects.all()
    serializer_class = AllUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


class AllFreeGamesApiView(generics.RetrieveAPIView):
    """Представление отдельного пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class RegisterApiView(generics.CreateAPIView):
#     """ Регистрация"""
#     serializer_class = RegisterSerializer
#     permission_classes = (permissions.AllowAny,)
#
#     def perform_create(self, serializer, *args, **kwargs):
#         user = serializer.save()
#         user.set_password(user.password)
#         user.save()
