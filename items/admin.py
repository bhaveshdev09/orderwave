# admin.py
from django.contrib import admin
from items.models import (
    Section,
    Category,
)


class SectionAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


admin.site.register(Section, SectionAdmin)
admin.site.register(Category, CategoryAdmin)
