from django.urls import path
from .views import NewsApiView

app_name = 'news'

urlpatterns = [
    path('news/<int:pk>/', NewsApiView.as_view(), name="Новость")
]
