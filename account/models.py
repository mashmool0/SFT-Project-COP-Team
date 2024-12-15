from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message='شماره موبایل باید با 09 شروع شده و 11 رقم باشد'
            )
        ]
    )
    is_phone_verified = models.BooleanField(default=False)

    # اطلاعات شخصی
    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')

    # اطلاعات تکمیلی
    DEGREE_CHOICES = [
        ('diploma', 'دیپلم'),
        ('bachelor', 'کارشناسی'),
        ('master', 'کارشناسی ارشد'),
        ('phd', 'دکتری'),
    ]

    field_of_study = models.CharField(
        max_length=100,
        verbose_name='رشته تحصیلی',
        blank=True
    )
    degree = models.CharField(
        max_length=20,
        choices=DEGREE_CHOICES,
        verbose_name='مقطع تحصیلی',
        blank=True
    )
    city = models.CharField(
        max_length=50,
        verbose_name='شهر محل سکونت',
        blank=True
    )

    # علاقه‌مندی‌ها
    INTEREST_CHOICES = [
        ('technology', 'تکنولوژی'),
        ('business', 'کسب و کار'),
        ('art', 'هنر'),
        ('science', 'علوم'),
        ('health', 'سلامت'),
        ('education', 'آموزش'),
        ('other', 'سایر')
    ]

    interests = MultiSelectField(
        choices=INTEREST_CHOICES,
        max_choices=5,
        max_length=100,
        verbose_name='علاقه‌مندی‌ها',
        blank=True
    )
    other_interests = models.CharField(
        max_length=200,
        verbose_name='سایر علاقه‌مندی‌ها',
        blank=True
    )

    # فیلدهای پیشنهادی برای پیشنهاد رویدادها
    preferred_event_types = MultiSelectField(
        choices=[
            ('workshop', 'کارگاه'),
            ('seminar', 'سمینار'),
            ('conference', 'کنفرانس'),
            ('webinar', 'وبینار')
        ],
        max_choices=4,
        max_length=100,
        verbose_name='نوع رویدادهای مورد علاقه',
        blank=True
    )

    preferred_time_slots = MultiSelectField(
        choices=[
            ('morning', 'صبح'),
            ('afternoon', 'بعد از ظهر'),
            ('evening', 'عصر')
        ],
        max_choices=3,
        max_length=50,
        verbose_name='زمان‌های ترجیحی',
        blank=True
    )

    max_event_price = models.PositiveIntegerField(
        verbose_name='حداکثر هزینه قابل پرداخت برای رویداد',
        null=True,
        blank=True
    )

    is_profile_completed = models.BooleanField(
        default=False,
        verbose_name='تکمیل پروفایل'
    )

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f"{self.get_full_name()} - {self.phone_number}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
