from django.contrib import admin
from .models import Branch


class BranchAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_deleted"]
    search_fields = ["name"]
    list_filter = ["is_deleted"]


admin.site.register(Branch, BranchAdmin)
