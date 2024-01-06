# forms.py
from django import forms
from customers.models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.RegexField(
        strip=True,
        min_length=2,
        max_length=30,
        regex=r"^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$",
        error_messages={"invalid": "Enter a valid name."},
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

    class Meta:
        model = Customer
        fields = ["name", "mobile", "email"]
