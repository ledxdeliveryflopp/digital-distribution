from rest_framework.serializers import ModelSerializer
from .models import LanguageText, LanguageVoice, LanguageSubtitles


class AllLanguageTextSerializer(ModelSerializer):
    """Сериалайрез списка языков текста"""

    class Meta:
        model = LanguageText
        fields = '__all__'


class LanguageTextSerializer(ModelSerializer):
    """Сериалайрез отдельного языка текста"""

    class Meta:
        model = LanguageText
        fields = '__all__'


class AllLanguageVoiceSerializer(ModelSerializer):
    """Сериалайрез списка языков озвучки"""

    class Meta:
        model = LanguageVoice
        fields = '__all__'


class LanguageVoiceSerializer(ModelSerializer):
    """Сериалайрез отдельного языка озвучки"""

    class Meta:
        model = LanguageVoice
        fields = '__all__'


class AllLanguageSubtitlesSerializer(ModelSerializer):
    """Сериалайрез списка языков субтитров"""

    class Meta:
        model = LanguageSubtitles
        fields = '__all__'


class LanguageSubtitlesSerializer(ModelSerializer):
    """Сериалайрез отдельного языка субтитров"""

    class Meta:
        model = LanguageSubtitles
        fields = '__all__'
