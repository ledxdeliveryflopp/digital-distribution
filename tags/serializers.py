from rest_framework.serializers import ModelSerializer
from .models import Tags


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
