from django.contrib import admin

from backend.api.models import Profit


@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    list_display = ('image', 'description',)
