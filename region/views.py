from rest_framework import generics, filters
from .models import Region
from .serializers import ALLRegionsSerializer, RegionSerializer


class AllRegionsApiView(generics.ListAPIView):
    """Представление всех регионов"""
    queryset = Region.objects.all()
    serializer_class = ALLRegionsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class RegionApiView(generics.RetrieveAPIView):
    """Представление отдельного региона"""
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
