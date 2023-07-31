from django.urls import path
from .views import AllGamesApiView, GamesApiView, AllFreeGamesApiView, AllDiscountGamesApiView, AllNewGamesApiView

app_name = 'games'

urlpatterns = [
    path('all_games/', AllGamesApiView.as_view(), name="Все игры"),
    path('game/<int:pk>/', GamesApiView.as_view(), name="Игра"),
    path('all_free_games/', AllFreeGamesApiView.as_view(), name="Все бесплатные игры"),
    path('all_discount_games/', AllDiscountGamesApiView.as_view(), name="Все игры по скидке"),
    path('all_new_games/', AllNewGamesApiView.as_view(), name="Все игры по скидке"),
]
