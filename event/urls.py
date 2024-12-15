from django.urls import path
from .views import event_view, speaker_detail, speaker_list, like_event, add_comment

app_name = 'event'
urlpatterns = [
    path('<str:pk>', event_view, name='event'),
    path('speakers/', speaker_list, name='speaker_list'),  # صفحه لیست سخنران‌ها
    path('speaker/<int:pk>/', speaker_detail, name='speaker_detail'),  # جزئیات سخنران
    path('like/<int:event_id>/', like_event, name='like_event'),
    path('comment/<int:event_id>/', add_comment, name='add_comment'),
]
