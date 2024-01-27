# forms.py
from django import forms
from users.models import CustomUser
from branches.models import Branch


class CustomUserForm(forms.ModelForm):
    # branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ("name", "email", "mobile_no", "assigned_branch")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "autofocus": True,
                }
            ),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "assigned_branch": forms.Select(attrs={"class": "form-control"}),
        }


class CustomUserAuthForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = CustomUser
        fields = ["email", "password"]
