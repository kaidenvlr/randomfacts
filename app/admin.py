from django.contrib import admin

from app.models import Fact


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ['id', 'fact_title']
    search_fields = ['id']
