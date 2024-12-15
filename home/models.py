from django.db import models
from event.models import University, Major


class Speaker(models.Model):
    image = models.ImageField(upload_to='speaker_image/', blank=True, null=True)
    fullname = models.CharField(max_length=100)
    linkedin_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname


class Event(models.Model):
    TYPE_OF_EVENT = (
        ("kargah", "کارگاه"),
        ("seminar", "سمینار"),
        ("conferance", "کنفرانس"),
        ("dore", "دوره"),
        ("webinar", "وبینار"),
        ("bootcamp", "بوتکمپ"),
    )

    title = models.CharField(max_length=100)
    small_desc = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='event_image/')
    kondaktor = models.TextField(blank=True, null=True)
    speakers = models.ManyToManyField(Speaker, related_name='event_speaker')
    likes = models.PositiveIntegerField(default=0)
    university = models.ForeignKey(University, models.SET_NULL, related_name='event_uni', blank=True, null=True)
    type_of_event = models.CharField(choices=TYPE_OF_EVENT, blank=True, null=True, max_length=100)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, related_name='event_major', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    COMMENT_TYPE_CHOICES = [
        ('general', 'نظر عادی'),
        ('approved', 'نظر تایید شده'),
        ('expert', 'نظر متخصص'),
        ('ai', 'نظر هوش مصنوعی'),
        # Add more types as needed
    ]

    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    comment_type = models.CharField(max_length=20, choices=COMMENT_TYPE_CHOICES, default='general')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_comment_type_display()} - {self.text[:30]} {self.event.title}'
