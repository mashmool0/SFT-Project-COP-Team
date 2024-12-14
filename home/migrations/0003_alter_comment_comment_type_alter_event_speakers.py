# Generated by Django 5.1.4 on 2024-12-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_event_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_type',
            field=models.CharField(choices=[('general', 'نظرات عادی'), ('approved', 'نظرات تایید شده'), ('expert', 'نظرات متخصصین'), ('ai', 'نظر هوش مصنوعی')], default='general', max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(related_name='event_speaker', to='home.speaker'),
        ),
    ]
