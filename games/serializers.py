from rest_framework.serializers import ModelSerializer
from .models import Game, Tags, DownloadableContent


class ALLGamesSerializer(ModelSerializer):
    """Сериалайрез списка игр"""

    class Meta:
        model = Game
        fields = ['title', 'title_image', 'price', 'sale', 'discount', 'price_discount']


class GameSerializer(ModelSerializer):
    """Сериалайрез отдельной игры"""

    class Meta:
        model = Game
        fields = '__all__'


class ALLTagsSerializer(ModelSerializer):
    """Сериалайрез списка меток"""

    class Meta:
        model = Tags
        fields = '__all__'


class TagsSerializer(ModelSerializer):
    """Сериалайрез отдельной метки"""

    class Meta:
        model = Tags
        fields = ['title']


class ALLDownloadableContentSerializer(ModelSerializer):
    """Сериалайрез списка загружаемого контента"""

    class Meta:
        model = DownloadableContent
        fields = ['title', 'title_image', 'price', 'game']


class DownloadableContentSerializer(ModelSerializer):
    """Сериалайрез отдельного загружаемого контента"""

    class Meta:
        model = DownloadableContent
        fields = ['title', 'short_description', 'full_description', 'price', 'sale', 'discount', 'price_discount',
                  'min_system_requirements', 'release_date', 'tags', 'developer', 'title_image', 'images', 'trailer',
                  'game']
