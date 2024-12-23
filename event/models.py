from django.db import models


# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True
                                   )

    def __str__(self):
        return f'{self.name}'


class Major(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
