from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('language.urls', namespace='language')),
    path('api/v1/', include('tags.urls', namespace='tags')),
    path('api/v1/', include('games.urls', namespace='games')),
    path('api/v1/', include('news.urls', namespace='news')),
    path('api/v1/', include('dls.urls', namespace='dls')),
    path('api/v1/', include('developers.urls', namespace='developers')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
