from rest_framework.serializers import ModelSerializer
from .models import Region


class ALLRegionsSerializer(ModelSerializer):
    """Сериализатор всех регионов"""

    class Meta:
        model = Region
        exclude = ['games']


class RegionSerializer(ModelSerializer):
    """Сериализатор отдельного региона"""

    class Meta:
        model = Region
        fields = '__all__'
