from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Event, University, Major


def home_view(request):
    # فیلترها
    university_id = request.GET.get('university')
    major_id = request.GET.get('major')
    event_type = request.GET.get('event_type')

    # بارگذاری رویدادها با اعمال فیلترها
    event_list = Event.objects.all()

    # اعمال فیلترهای انتخابی روی رویدادها
    if university_id:
        event_list = event_list.filter(university_id=university_id)
    if major_id:
        event_list = event_list.filter(major_id=major_id)
    if event_type:
        event_list = event_list.filter(type=event_type)

    paginator = Paginator(event_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    universities = University.objects.all()
    majors = Major.objects.all()

    context = {
        'events': page_obj,
        'universities': universities,
        'majors': majors,
        'page_obj': page_obj,
    }
    return render(request, 'home/home.html', context)
