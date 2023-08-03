from django.urls import path
from .views import AllRegionsApiView, RegionApiView

app_name = 'region'

urlpatterns = [
    path('all_regions/', AllRegionsApiView.as_view(), name="Все регионы"),
    path('region/<int:pk>', RegionApiView.as_view(), name="Отдельный регион")

]
