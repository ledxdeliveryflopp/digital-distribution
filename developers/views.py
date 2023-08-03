from rest_framework import generics
from .models import DeveloperCompany
from .serializers import DeveloperCompanySerializer, AllDeveloperCompanySerializer


class AllDeveloperCompanyApiView(generics.ListAPIView):
    """Представление всеъ компаний"""
    queryset = DeveloperCompany.objects.all()
    serializer_class = DeveloperCompanySerializer


class DeveloperCompanyApiView(generics.RetrieveAPIView):
    """Представление отдельной компании"""
    queryset = DeveloperCompany.objects.all()
    serializer_class = AllDeveloperCompanySerializer

