from django.urls import path
from .views import AllGamesApiView, GamesApiView, AllTagsApiView, TagsApiView, AllDownloadableContentApiView, \
    DownloadableContentApiView, AllFreeGamesApiView

app_name = 'games'

urlpatterns = [
    path('all_games/', AllGamesApiView.as_view(), name="Все игры"),
    path('all_free_games/', AllFreeGamesApiView.as_view(), name="Все бесплатные игры"),
    path('game/<int:pk>/', GamesApiView.as_view(), name="Игра"),
    path('all_tags/', AllTagsApiView.as_view(), name="Все метки"),
    path('tag/<int:pk>/', TagsApiView.as_view(), name="Метка"),
    path('all_downloadable_content/', AllDownloadableContentApiView.as_view(),
         name="Все дополнительные загружаемые контенты"),
    path('downloadable_content/<int:pk>/', DownloadableContentApiView.as_view(),
         name="Дополниительый загружаемый контент"),
]
