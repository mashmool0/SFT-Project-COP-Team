# home/views.py
from django.shortcuts import render
from .models import Event


def home_view(request):
    events = Event.objects.all()
    return render(request, 'home/home.html', context={'events': events})
