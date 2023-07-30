from django.urls import path
from .views import DeveloperCompanyApiView, AllDeveloperCompanyApiView

app_name = 'developers'

urlpatterns = [
    path('all_company/', AllDeveloperCompanyApiView.as_view(), name="Все компании разработчики"),
    path('company/<int:pk>/', DeveloperCompanyApiView.as_view(), name="Компания разработчик"),
]
