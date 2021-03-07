from django.contrib import admin

from . import models

admin.site.register(models.Profit)
admin.site.register(models.Service)
admin.site.register(models.Site)
admin.site.register(models.Advertisement)


@admin.register(models.Consultation)
class ConsultationManager(admin.ModelAdmin):
    list_display = ('id', 'service', 'full_name', 'telephone_number', 'status', 'receipted_time',
                    'response_time',)


@admin.register(models.Application)
class ApplicationManager(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'telephone_number', 'status', 'receipted_time', 'response_time',)
