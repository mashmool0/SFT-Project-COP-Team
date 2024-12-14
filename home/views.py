# home/views.py
from django.shortcuts import render
from .models import Event

from django.core.paginator import Paginator

from .models import Event, University

# home/views.py
from django.shortcuts import render
from .models import Event

from django.core.paginator import Paginator

from .models import Event, University


def home_view(request):
    event_list = Event.objects.all()
    universities = University.objects.all()  # بارگذاری دانشگاه‌ها
    paginator = Paginator(event_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'events': page_obj,
        'universities': universities,  # اضافه کردن دانشگاه‌ها به context
        'page_obj': page_obj,
    }
    return render(request, 'home/home.html', context)
