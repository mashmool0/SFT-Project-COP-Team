from django.urls import path
from .views import event_view, speaker_detail, speaker_list

app_name = 'event'
urlpatterns = [
    path('<str:pk>', event_view, name='event'),
    path('speakers/', speaker_list, name='speaker_list'),  # صفحه لیست سخنران‌ها
    path('speaker/<int:pk>/', speaker_detail, name='speaker_detail'),  # جزئیات سخنران
]
