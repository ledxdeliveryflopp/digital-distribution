from rest_framework import generics, filters
from .models import Game, Tags
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ALLGamesSerializer, GameSerializer, ALLTagsSerializer, TagsSerializer


class AllGamesApiView(generics.ListAPIView):
    """Представление всех игр"""
    queryset = Game.objects.all()
    serializer_class = ALLGamesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'developer__title', 'tags__title']
    permission_classes = (AllowAny,)


class AllFreeGamesApiView(generics.ListAPIView):
    """Представление всех бесплатных игр"""
    queryset = Game.objects.exclude(price=0)
    serializer_class = ALLGamesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'developer__title', 'tags__title']
    permission_classes = (AllowAny,)


class AllDiscountGamesApiView(generics.ListAPIView):
    """Представление всех игр по скидке"""
    queryset = Game.objects.filter(sale=True)
    serializer_class = ALLGamesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'developer__title', 'tags__title']
    permission_classes = (AllowAny,)


class AllNewGamesApiView(generics.ListAPIView):
    """Представление всех новых игр"""
    queryset = Game.objects.filter(new_game=True)
    serializer_class = ALLGamesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'developer__title', 'tags__title']
    permission_classes = (AllowAny,)


class GamesApiView(generics.RetrieveAPIView):
    """Представление отдельной игры"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (AllowAny,)



