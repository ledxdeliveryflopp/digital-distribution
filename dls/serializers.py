from rest_framework.serializers import ModelSerializer
from .models import DownloadableContent


class ALLDownloadableContentSerializer(ModelSerializer):
    """Сериалайрез списка загружаемого контента"""

    class Meta:
        model = DownloadableContent
        fields = ['title', 'title_image', 'price', 'game']


class DownloadableContentSerializer(ModelSerializer):
    """Сериалайрез отдельного загружаемого контента"""

    class Meta:
        model = DownloadableContent
        fields = ['title', 'short_description', 'full_description', 'language_text', 'language_voice',
                  'language_subtitles', 'price', 'sale', 'discount', 'price_discount', 'min_system_requirements',
                  'req_system_requirements', 'release_date', 'tags', 'developer', 'title_image', 'images', 'trailer',
                  'game']
