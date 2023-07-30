from rest_framework import generics
from .models import DeveloperCompany
from .serializers import DeveloperCompanySerializer, AllDeveloperCompanySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class AllDeveloperCompanyApiView(generics.ListAPIView):
    """Представление всеъ компаний"""
    queryset = DeveloperCompany.objects.all()
    serializer_class = DeveloperCompanySerializer
    permission_classes = (AllowAny,)


class DeveloperCompanyApiView(generics.RetrieveAPIView):
    """Представление отдельной компании"""
    queryset = DeveloperCompany.objects.all()
    serializer_class = AllDeveloperCompanySerializer
    permission_classes = (AllowAny,)

