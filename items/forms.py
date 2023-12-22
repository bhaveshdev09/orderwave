from django import forms
from items.models import (
    Section,
    Category,
    OperatingHour,
    Item,
)


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["title"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]


class OperatingHourForm(forms.ModelForm):
    class Meta:
        model = OperatingHour
        fields = ["from_time", "to_time", "tags", "title"]


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "desc",
            "section",
            "category",
            "operation_hour",
            "base_price",
        ]
