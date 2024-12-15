from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import jdatetime
from .models import Event, University, Major


def jalali_to_gregorian(jdate_str):
    """تبدیل تاریخ شمسی به میلادی"""
    try:
        j_date = jdatetime.datetime.strptime(jdate_str, '%Y/%m/%d').togregorian()
        return j_date.date()
    except (ValueError, TypeError):
        return None


def filter_events(request, queryset):
    """
    فانکشن پایه برای اعمال فیلترها روی کوئری‌ست رویدادها
    """
    # دریافت پارامترهای فیلتر از ریکوئست
    university_id = request.GET.get('university')
    major_id = request.GET.get('major')
    event_type = request.GET.get('event_type')
    search_query = request.GET.get('search')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    # اعمال فیلترهای پایه
    if university_id:
        queryset = queryset.filter(university_id=university_id)
    if major_id:
        queryset = queryset.filter(major_id=major_id)
    if event_type:
        queryset = queryset.filter(type_of_event=event_type)

    # جستجو در عنوان و توضیحات
    if search_query:
        queryset = queryset.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # فیلتر تاریخ
    if date_from:
        g_date = jalali_to_gregorian(date_from)
        if g_date:
            queryset = queryset.filter(date_of_event__date__gte=g_date)

    if date_to:
        g_date = jalali_to_gregorian(date_to)
        if g_date:
            queryset = queryset.filter(date_of_event__date__lte=g_date)

    return queryset


def home_view(request):
    """
    نمایش صفحه اصلی با لیست رویدادها و فیلترها
    """
    # دریافت تمام رویدادها و اعمال فیلترها
    event_list = Event.objects.all().order_by('-date_of_event')
    filtered_events = filter_events(request, event_list)

    # تنظیمات صفحه‌بندی
    items_per_page = 10  # تعداد آیتم در هر صفحه
    paginator = Paginator(filtered_events, items_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # دریافت لیست دانشگاه‌ها و رشته‌ها برای فیلترها
    universities = University.objects.all()
    majors = Major.objects.all()

    # تنظیم مقادیر فیلترهای انتخاب شده برای نمایش در فرم
    selected_filters = {
        'university': request.GET.get('university', ''),
        'major': request.GET.get('major', ''),
        'event_type': request.GET.get('event_type', ''),
        'search': request.GET.get('search', ''),
        'date_from': request.GET.get('date_from', ''),
        'date_to': request.GET.get('date_to', ''),
    }

    # انواع رویدادها (این مقادیر باید با مقادیر تعریف شده در مدل Event هماهنگ باشند)
    EVENT_TYPES = [
        ('seminar', 'سمینار'),
        ('workshop', 'کارگاه'),
        ('conference', 'کنفرانس'),
        ('meeting', 'جلسه'),
        ('other', 'سایر'),
    ]

    context = {
        'events': page_obj,
        'universities': universities,
        'majors': majors,
        'page_obj': page_obj,
        'selected_filters': selected_filters,
        'event_types': EVENT_TYPES,
    }

    return render(request, 'home/home.html', context)
