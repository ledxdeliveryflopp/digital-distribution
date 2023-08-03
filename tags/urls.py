from django.urls import path
from .views import AllTagsApiView, TagsApiView

app_name = 'tags'

urlpatterns = [
    path('all_tags/', AllTagsApiView.as_view(), name="Все метки"),
    path('tag/<int:pk>/', TagsApiView.as_view(), name="Метка"),
]
