from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import Tags
from .serializers import ALLTagsSerializer, TagsSerializer


class AllTagsApiView(generics.ListAPIView):
    """Представление всех меток"""
    queryset = Tags.objects.all()
    serializer_class = ALLTagsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (AllowAny,)


class TagsApiView(generics.RetrieveAPIView):
    """Представление отдельной метки"""
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)
