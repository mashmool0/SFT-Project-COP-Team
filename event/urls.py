from django.urls import path
from .views import event_view

app_name = 'event'
urlpatterns = [
    path('<str:pk>', event_view, name='event'),
]
