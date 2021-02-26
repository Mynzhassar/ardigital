from django.db import models


class Profit(models.Model):
    image = models.ImageField(upload_to='profits')
    description = models.TextField(max_length=100)

    objects = models.Manager()

    class Meta:
        verbose_name = 'profit'
        verbose_name_plural = 'profits'

    def __str__(self):
        return self.description
