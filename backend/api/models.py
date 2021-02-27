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
