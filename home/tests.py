import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'COP.settings')
django.setup()

import random
from django.core.files.base import ContentFile
import requests
from django.utils import timezone
from datetime import timedelta
from faker import Faker
from home.models import Speaker, Event, Comment
from event.models import University, Major


def get_random_image(width=800, height=600):
    response = requests.get(f'https://picsum.photos/{width}/{height}')
    if response.status_code == 200:
        return ContentFile(response.content, name=f'image_{random.randint(1, 1000)}.jpg')
    return None


def generate_fake_data():
    fake = Faker(['fa_IR'])

    # ساخت دانشگاه‌ها
    universities = [
        "دانشگاه تهران",
        "دانشگاه صنعتی شریف",
        "دانشگاه امیرکبیر",
        "دانشگاه علم و صنعت",
        "دانشگاه شهید بهشتی",
    ]

    for uni_name in universities:
        University.objects.create(
            name=uni_name,
            description=fake.text(max_nb_chars=200)
        )

    # ساخت رشته‌های تحصیلی
    majors = [
        "مهندسی کامپیوتر",
        "مهندسی برق",
        "مهندسی مکانیک",
        "مهندسی عمران",
        "علوم کامپیوتر",
        "هوش مصنوعی",
        "مهندسی پزشکی",
    ]

    for major_name in majors:
        Major.objects.create(
            name=major_name,
            desc=fake.text(max_nb_chars=300)
        )

    # ساخت سخنران‌ها
    speaker_descriptions = [
        "متخصص هوش مصنوعی و یادگیری ماشین با ۱۰ سال سابقه در گوگل",
        "مدرس دانشگاه و پژوهشگر حوزه بلاکچین",
        "توسعه‌دهنده ارشد و مشاور استارتاپ‌های موفق",
        "متخصص امنیت سایبری و مدیر فنی",
        "کارآفرین موفق و بنیانگذار چندین استارتاپ",
    ]

    for i in range(10):
        Speaker.objects.create(
            image=get_random_image(400, 400),
            fullname=fake.name(),
            linkedin_url=f"https://linkedin.com/in/{fake.user_name()}",
            description=random.choice(speaker_descriptions)
        )

    # ساخت رویدادها
    event_titles = [
        "کارگاه پایتون پیشرفته",
        "همایش هوش مصنوعی و آینده",
        "دوره جامع DevOps",
        "کنفرانس بلاکچین و رمزارزها",
        "بوتکمپ برنامه‌نویسی وب",
        "وبینار امنیت سایبری",
    ]

    for i in range(15):
        event = Event.objects.create(
            title=random.choice(event_titles) + f" {i + 1}",
            small_desc=fake.sentence(),
            description=fake.text(max_nb_chars=500),
            image=get_random_image(),
            kondaktor=fake.name(),
            likes=random.randint(10, 1000),
            university=University.objects.order_by('?').first(),
            type_of_event=random.choice([x[0] for x in Event.TYPE_OF_EVENT]),
            major=Major.objects.order_by('?').first(),
            date_of_event=timezone.now() + timedelta(days=random.randint(1, 60))
        )
        # اضافه کردن سخنران‌ها به رویداد
        speakers = Speaker.objects.order_by('?')[:random.randint(1, 3)]
        event.speakers.add(*speakers)

    # ساخت نظرات
    comment_texts = [
        "عالی بود! خیلی استفاده کردم",
        "مطالب کاربردی و مفید بود",
        "کاش زمان بیشتری داشت",
        "سخنران تسلط خوبی داشت",
        "محتوا خیلی غنی بود",
    ]

    for event in Event.objects.all():
        for _ in range(random.randint(3, 8)):
            Comment.objects.create(
                event=event,
                text=random.choice(comment_texts) + " " + fake.sentence(),
                comment_type=random.choice([x[0] for x in Comment.COMMENT_TYPE_CHOICES]),
                created_at=event.created_at + timedelta(days=random.randint(1, 10))
            )

    print("✅ Data generation completed successfully!")
    print(f"\nStatistics:")
    print(f"Universities: {University.objects.count()}")
    print(f"Majors: {Major.objects.count()}")
    print(f"Speakers: {Speaker.objects.count()}")
    print(f"Events: {Event.objects.count()}")
    print(f"Comments: {Comment.objects.count()}")


if __name__ == '__main__':
    generate_fake_data()