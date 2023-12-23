# forms.py
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from branches.models import Branch


class CustomUserForm(forms.ModelForm):
    # branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=False)
    class Meta:
        model = CustomUser
        fields = ("name", "email", "mobile_no", "branch")
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "branch": forms.Select(attrs={"class": "form-control"}),
        }
