from rest_framework.serializers import ModelSerializer
from .models import News


class NewsSerializer(ModelSerializer):
    """Сериалайрез отдельной новости"""

    class Meta:
        model = News
        fields = '__all__'


