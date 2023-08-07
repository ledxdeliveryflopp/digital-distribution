from rest_framework import generics
from .models import LanguageText, LanguageVoice, LanguageSubtitles
from .serializers import AllLanguageTextSerializer, LanguageTextSerializer, AllLanguageVoiceSerializer, \
    LanguageVoiceSerializer, LanguageSubtitlesSerializer, AllLanguageSubtitlesSerializer


class AllLanguageTextApiView(generics.ListAPIView):
    """Представление всех языков текста"""
    queryset = LanguageText.objects.all()
    serializer_class = AllLanguageTextSerializer


class LanguageTextApiView(generics.RetrieveAPIView):
    """Представление отдельного языка текста"""
    queryset = LanguageText.objects.all()
    serializer_class = LanguageTextSerializer


class AllLanguageVoiceApiView(generics.ListAPIView):
    """Представление всех языков озвучки"""
    queryset = LanguageVoice.objects.all()
    serializer_class = AllLanguageVoiceSerializer


class LanguageVoiceApiView(generics.RetrieveAPIView):
    """Представление отдельного языка озвучки"""
    queryset = LanguageVoice.objects.all()
    serializer_class = LanguageVoiceSerializer


class AllLanguageSubtitlesApiView(generics.ListAPIView):
    """Представление всех языков субтитров"""
    queryset = LanguageSubtitles.objects.all()
    serializer_class = AllLanguageSubtitlesSerializer


class LanguageSubtitlesApiView(generics.RetrieveAPIView):
    """Представление отдельного языка субтитров"""
    queryset = LanguageSubtitles.objects.all()
    serializer_class = LanguageSubtitlesSerializer