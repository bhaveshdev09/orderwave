from django import forms
from materials.models import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["name", "units", "price"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "units": forms.Select(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }
