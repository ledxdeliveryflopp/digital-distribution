from rest_framework import generics, filters
from .models import News
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import NewsSerializer


class NewsApiView(generics.RetrieveAPIView):
    """Представление отдельной новости"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (AllowAny,)

