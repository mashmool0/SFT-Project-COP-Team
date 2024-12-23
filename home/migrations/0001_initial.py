# Generated by Django 5.1.4 on 2024-12-15 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='speaker_image/')),
                ('fullname', models.CharField(max_length=100)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('small_desc', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='event_image/')),
                ('kondaktor', models.TextField(blank=True, null=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('type_of_event', models.CharField(blank=True, choices=[('kargah', 'کارگاه'), ('seminar', 'سمینار'), ('conferance', 'کنفرانس'), ('dore', 'دوره'), ('webinar', 'وبینار'), ('bootcamp', 'بوتکمپ')], max_length=100, null=True)),
                ('date_of_event', models.DateTimeField(blank=True, null=True)),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_major', to='event.major')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_uni', to='event.university')),
                ('speakers', models.ManyToManyField(related_name='event_speaker', to='home.speaker')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('comment_type', models.CharField(choices=[('general', 'نظر عادی'), ('approved', 'نظر تایید شده'), ('expert', 'نظر متخصص'), ('ai', 'نظر هوش مصنوعی')], default='general', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.event')),
            ],
        ),
    ]
