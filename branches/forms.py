from django import forms
from branches.models import Branch


class BranchForm(forms.ModelForm):
    name = forms.RegexField(
        strip=True,
        min_length=2,
        max_length=20,
        regex="^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Branch Name",
                "pattern": "^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$",
            }
        ),
    )

    # TODO: Resolve unique constraints error for slug (i.e add "Mumbai" again)
    class Meta:
        model = Branch
        fields = ("name",)
