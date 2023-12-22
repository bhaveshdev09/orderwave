from django import forms
from items.models import (
    Section,
    Category,
)


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["title"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]
