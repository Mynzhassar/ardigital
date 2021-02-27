from django.contrib import admin

from . import models


@admin.register(models.Profit)
class ProfitAdmin(admin.ModelAdmin):
    list_display = ('image', 'description',)


@admin.register(models.Service)
class ServiceManager(admin.ModelAdmin):
    list_display = ('title', 'image', 'description',)


@admin.register(models.Consultation)
class ConsultationManager(admin.ModelAdmin):
    list_display = (
        'service', 'full_name', 'telephone_number', 'status', 'receipted_time', 'response_time',)
