from django.contrib import admin

from .models import Profit, Service


@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    list_display = ('image', 'description',)


@admin.register(Service)
class ServiceManager(admin.ModelAdmin):
    list_display = ('title', 'image', 'description',)
