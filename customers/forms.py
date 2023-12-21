# forms.py
from django import forms
from customers.models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField(strip=True, min_length=2, max_length=20)
    mobile = forms.CharField(strip=True, min_length=10, max_length=12)

    class Meta:
        model = Customer
        fields = ["name", "mobile", "email"]
