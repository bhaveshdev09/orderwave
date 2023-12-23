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
        widgets = {
            "from_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
            "to_time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "tags": forms.Select(attrs={"class": "form-control"}),
        }


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
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "desc": forms.Textarea(attrs={"class": "form-control"}),
            "section": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "operation_hour": forms.Select(attrs={"class": "form-control"}),
            "base_price": forms.NumberInput(attrs={"class": "form-control"}),
        }
