from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import AllUserApiView, AllFreeGamesApiView, RegisterApiView

app_name = 'user'

urlpatterns = [
    path('all_users/', AllUserApiView.as_view(), name="Все пользователи"),
    path('user/<int:pk>', AllFreeGamesApiView.as_view(), name="Отдельный пользователь"),
    path('obtain_token/', TokenObtainPairView.as_view(), name='login'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token_add_blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('register/', RegisterApiView.as_view(), name='регистрация')
]
