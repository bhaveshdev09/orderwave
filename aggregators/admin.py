from django.contrib import admin
from aggregators.models import Aggregator


class AggregatorAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_deleted"]
    search_fields = ["name"]
    list_filter = ["is_deleted"]


admin.site.register(Aggregator, AggregatorAdmin)
