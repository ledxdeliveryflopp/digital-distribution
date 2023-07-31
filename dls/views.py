from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import DownloadableContent
from .serializers import ALLDownloadableContentSerializer, DownloadableContentSerializer


class AllDownloadableContentApiView(generics.ListAPIView):
    """Представление всех дополнительных загружаемых контентов"""
    queryset = DownloadableContent.objects.all()
    serializer_class = ALLDownloadableContentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (AllowAny,)


class DownloadableContentApiView(generics.RetrieveAPIView):
    """Представление отдельного загружаемого контента"""
    queryset = DownloadableContent.objects.all()
    serializer_class = DownloadableContentSerializer
    permission_classes = (AllowAny,)
