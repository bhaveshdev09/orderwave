from django import forms
from materials.models import Material


class MaterialForm(forms.ModelForm):
    name = forms.RegexField(
        strip=True,
        min_length=2,
        max_length=20,
        regex=r"^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$",
        error_messages={
            "invalid": "Enter a valid name.",
            "unique": "Material name already exists.Please provide a different one.",
        },
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                # "placeholder": "Enter Vendor Name",
                "pattern": "^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$",
                "autofocus": True,
            }
        ),
    )
    price = forms.FloatField(
        min_value=1.0,
        required=True,
        initial=1.0,
        error_messages={"invalid": "Enter a valid price."},
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.5"}),
    )
    units = forms.ChoiceField(
        choices=Material.UNIT_CHOICES,
        initial=Material.UNIT_CHOICE_UNITS,
        widget=forms.Select(attrs={"class": "form-select select"}),
    )
    # units = forms.CharField(widget=forms.Select(attrs={"class": "form-select select"}))

    class Meta:
        model = Material
        fields = ["name", "units", "price"]
