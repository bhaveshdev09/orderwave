# admin.py
from django.contrib import admin
from items.models import Section, Category, OperatingHour, Item


class SectionAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


class OperatingHourAdmin(admin.ModelAdmin):
    list_display = ["title", "from_time", "to_time", "tags"]
    search_fields = ["title"]


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "section", "category", "base_price", "tax", "selling_price"]
    search_fields = ["name", "section__title", "category__title"]

    def selling_price(self, obj):
        return (
            obj.selling_price
        )  # Assuming you have a selling_price property in the Item model

    selling_price.short_description = "Selling Price"


admin.site.register(Section, SectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OperatingHour, OperatingHourAdmin)
admin.site.register(Item, ItemAdmin)
