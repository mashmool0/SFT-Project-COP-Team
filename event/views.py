# Django view - views.py
from django.shortcuts import render, redirect
from home.models import Event


def event_view(request, pk):
    try:
        event = Event.objects.get(id=pk)
        speakers = event.speakers.all()  # Assuming a related name 'speaker_set'
        comments = event.comments.all()  # Assuming a related name 'comment_set'
        context = {
            'event': event,
            'speakers': speakers,
            'comments': comments,
        }
        return render(request, 'event/event.html', context=context)
    except Event.DoesNotExist:
        return redirect("home:home")
