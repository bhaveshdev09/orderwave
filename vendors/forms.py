from django import forms
from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["name", "addr", "mobile", "email"]

    widgets = {
        "name": forms.TextInput(attrs={"class": "form-control"}),
        "email": forms.EmailInput(attrs={"class": "form-control"}),
        "mobile": forms.TextInput(attrs={"class": "form-control"}),
    }
