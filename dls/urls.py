from django.urls import path
from .views import AllDownloadableContentApiView,DownloadableContentApiView

app_name = 'dls'

urlpatterns = [
    path('all_downloadable_content/', AllDownloadableContentApiView.as_view(),
         name="Все дополнительные загружаемые контенты"),
    path('downloadable_content/<int:pk>/', DownloadableContentApiView.as_view(),
         name="Дополниительый загружаемый контент"),
]
