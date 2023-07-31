from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import LanguageText, LanguageVoice, LanguageSubtitles
from .serializers import AllLanguageTextSerializer, LanguageTextSerializer, AllLanguageVoiceSerializer, \
    LanguageVoiceSerializer, LanguageSubtitlesSerializer, AllLanguageSubtitlesSerializer


class AllLanguageTextApiView(generics.ListAPIView):
    """Представление всех языков текста"""
    queryset = LanguageText.objects.all()
    serializer_class = AllLanguageTextSerializer
    permission_classes = (AllowAny,)


class LanguageTextApiView(generics.RetrieveAPIView):
    """Представление отдельного языка текста"""
    queryset = LanguageText.objects.all()
    serializer_class = LanguageTextSerializer
    permission_classes = (AllowAny,)


class AllLanguageVoiceApiView(generics.ListAPIView):
    """Представление всех языков озвучки"""
    queryset = LanguageVoice.objects.all()
    serializer_class = AllLanguageVoiceSerializer
    permission_classes = (AllowAny,)


class LanguageVoiceApiView(generics.RetrieveAPIView):
    """Представление отдельного языка озвучки"""
    queryset = LanguageVoice.objects.all()
    serializer_class = LanguageVoiceSerializer
    permission_classes = (AllowAny,)


class AllLanguageSubtitlesApiView(generics.ListAPIView):
    """Представление всех языков субтитров"""
    queryset = LanguageSubtitles.objects.all()
    serializer_class = AllLanguageSubtitlesSerializer
    permission_classes = (AllowAny,)


class LanguageSubtitlesApiView(generics.RetrieveAPIView):
    """Представление отдельного языка субтитров"""
    queryset = LanguageSubtitles.objects.all()
    serializer_class = LanguageSubtitlesSerializer
    permission_classes = (AllowAny,)
