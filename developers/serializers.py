from rest_framework.serializers import ModelSerializer
from .models import DeveloperCompany


class AllDeveloperCompanySerializer(ModelSerializer):
    """Сериалайрез всех компаний"""

    class Meta:
        model = DeveloperCompany
        fields = '__all__'


class DeveloperCompanySerializer(ModelSerializer):
    """Сериалайрез отдельной компании"""

    class Meta:
        model = DeveloperCompany
        fields = ['title', 'description']
