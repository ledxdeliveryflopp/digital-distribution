from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/', include('language.urls', namespace='language')),
    path('api/v2/', include('tags.urls', namespace='tags')),
    path('api/v2/', include('games.urls', namespace='games')),
    path('api/v2/', include('news.urls', namespace='news')),
    path('api/v2/', include('dls.urls', namespace='dls')),
    path('api/v2/', include('developers.urls', namespace='developers')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
