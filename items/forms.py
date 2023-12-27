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
    operation_hour = forms.ModelMultipleChoiceField(
        queryset=OperatingHour.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
            }
        ),
    )
    tax = forms.FloatField(
        initial=5.0, widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    base_price = forms.FloatField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Item
        fields = [
            "name",
            "section",
            "category",
            "operation_hour",
            "base_price",
            "tax",
            "desc",
            "is_active",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "desc": forms.Textarea(attrs={"class": "form-control"}),
            "section": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
