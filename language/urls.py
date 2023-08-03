from django.urls import path
from .views import AllLanguageTextApiView, LanguageTextApiView, AllLanguageVoiceApiView, LanguageVoiceApiView, \
    AllLanguageSubtitlesApiView, LanguageSubtitlesApiView

app_name = 'language'

urlpatterns = [
    path('all_lang_text/', AllLanguageTextApiView.as_view(), name="Все языки текста"),
    path('lang_text/<int:pk>/', LanguageTextApiView.as_view(), name="Язык текста"),
    path('all_lang_voice/', AllLanguageVoiceApiView.as_view(), name="Все языки озвучки"),
    path('lang_voice/<int:pk>/', LanguageVoiceApiView.as_view(), name="Язык озвучки"),
    path('all_lang_subtitles/', AllLanguageSubtitlesApiView.as_view(), name="Все языки субтитрорв"),
    path('lang_subtitles/<int:pk>/', LanguageSubtitlesApiView.as_view(), name="Язык субтитрорв"),
]
