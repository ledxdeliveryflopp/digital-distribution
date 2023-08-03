from rest_framework import generics, filters
from .models import Game
from .serializers import ALLGamesSerializer, GameSerializer


class AllGamesApiView(generics.ListAPIView):
    """Представление всех игр"""
    queryset = Game.objects.all()
    serializer_class = ALLGamesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'developer__title', 'tags__title']


class AllFreeGamesApiView(generics.ListAPIView):
    """Представление всех бесплатных игр"""
    queryset = Game.objects.exclude(price=0)
    serializer_class = ALLGamesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'developer__title', 'tags__title']


class AllDiscountGamesApiView(generics.ListAPIView):
    """Представление всех игр по скидке"""
    queryset = Game.objects.filter(sale=True)
    serializer_class = ALLGamesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'developer__title', 'tags__title']


class AllNewGamesApiView(generics.ListAPIView):
    """Представление всех новых игр"""
    queryset = Game.objects.filter(new_game=True)
    serializer_class = ALLGamesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'developer__title', 'tags__title']


class GamesApiView(generics.RetrieveAPIView):
    """Представление отдельной игры"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer



