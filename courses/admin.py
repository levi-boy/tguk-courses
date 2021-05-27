from django.contrib import admin

from .models import News, Record


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
