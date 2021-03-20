from django.db import models
from django.utils import timezone

from . import constants


class Profit(models.Model):
    image = models.ImageField(upload_to='media/profits')
    description = models.TextField(blank=False)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Профит'
        verbose_name_plural = 'Профит'

    def __str__(self):
        return self.description


class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/services')
    description = models.TextField(blank=False)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class Consultation(models.Model):
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                related_name='services')

    full_name = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=10,
                              choices=constants.CONSULTATION_STATUS_CHOICES,
                              default=constants.STATUS_NEW)

    receipted_time = models.DateTimeField(default=timezone.now)
    response_time = models.DateTimeField(null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'

    def __str__(self):
        return self.service.title


class Case(models.Model):
    description = models.TextField(blank=False)
    link = models.URLField()

    objects = models.Manager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.description


class Site(Case):
    image = models.ImageField(upload_to='media/sites')

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'


class Advertisement(Case):
    image = models.ImageField(upload_to='media/advertisements')

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'


class Application(models.Model):
    full_name = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=15,
                              choices=constants.APPLICATION_STATUS_CHOICES,
                              default=constants.STATUS_NEW)

    receipted_time = models.DateTimeField(default=timezone.now)
    response_time = models.DateTimeField(null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
