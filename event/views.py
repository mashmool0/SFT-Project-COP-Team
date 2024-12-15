from django.shortcuts import render, redirect
from home.models import Event, Speaker, Comment
from .models import University  # فرض بر این است که مدل دانشگاه تعریف شده باشد


def event_view(request, pk):
    try:
        event = Event.objects.get(id=pk)
        speakers = event.speakers.all()  # Assuming a related name 'speaker_set'
        comments = event.comments.all()  # Assuming a related name 'comment_set'

        # اطلاعات دانشگاه
        university = event.university  # اطلاعات دانشگاه مربوط به رویداد

        context = {
            'event': event,
            'speakers': speakers,
            'comments': comments,
            'university': university,  # اطلاعات دانشگاه
        }
        return render(request, 'event/event.html', context=context)
    except Event.DoesNotExist:
        return redirect("home:home")


def speaker_list(request):
    speakers = Speaker.objects.all()  # دریافت تمامی سخنران‌ها
    return render(request, 'event/speaker_list.html', {'speakers': speakers})


def speaker_detail(request, pk):
    try:
        speaker = Speaker.objects.get(id=pk)
        return render(request, 'event/speaker_detail.html', {'speaker': speaker})
    except Speaker.DoesNotExist:
        return redirect("home:home")


