from django import forms
from .models import Vendor


class VendorForm(forms.ModelForm):
    name = forms.RegexField(
        strip=True,
        min_length=2,
        max_length=20,
        regex=r"^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                # "placeholder": "Enter Vendor Name",
                "pattern": "^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$",
                "autofocus": True,
            }
        ),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    mobile = forms.RegexField(
        strip=True,
        error_messages={"invalid": "Enter a valid mobile number."},
        max_length=10,
        regex=r"^[6789]\d{9}$",  # The regex parameter uses a raw string (prefixed with r) for the regular expression pattern.
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "type": "tel", "pattern": "^[6789]\d{9}$"}
        ),
    )
    addr = forms.CharField(
        label="Address", widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Vendor
        fields = ["name", "addr", "mobile", "email"]
