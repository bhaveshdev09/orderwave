from django import forms
from items.models import Section, Category, OperatingHour


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
