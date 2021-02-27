from datetime import datetime
from django.db import models


class Profit(models.Model):
    image = models.ImageField(upload_to='profits')
    description = models.TextField(blank=False)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Профит'

    def __str__(self):
        return self.description


class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services')
    description = models.TextField(blank=False)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class Consultation(models.Model):
    NEW = 'NEW'
    PROCESSED = 'PROCESSED'

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    full_name = models.CharField(max_length=100)
    telephone_number = models.CharField()
    status = models.CharField(choices=[NEW, PROCESSED])
    receipted_time = models.DateTimeField(default=datetime.now())
    response_time = models.DateTimeField(null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'

    def __str__(self):
        return self.service
