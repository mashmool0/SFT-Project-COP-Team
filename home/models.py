from django.db import models


class Speaker(models.Model):
    image = models.ImageField(upload_to='speaker_image/', blank=True, null=True)
    fullname = models.CharField(max_length=100)
    linkedin_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname


class Event(models.Model):
    title = models.CharField(max_length=100)
    small_desc = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='event_image/')
    kondaktor = models.TextField(blank=True, null=True)
    speakers = models.ManyToManyField(Speaker, related_name='events')
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    COMMENT_TYPE_CHOICES = [
        ('general', 'نظرات عادی'),
        ('question', 'سؤالات'),
        ('suggestion', 'پیشنهادات'),
        ('approved', 'نظرات تایید شده'),
        ('expert', 'نظرات متخصصین'),
        ('ai', 'نظر هوش مصنوعی'),
        # Add more types as needed
    ]

    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    comment_type = models.CharField(max_length=20, choices=COMMENT_TYPE_CHOICES, default='general')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_comment_type_display()} - {self.text[:30]}'
