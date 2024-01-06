from django import forms
from aggregators.models import Aggregator


class AggregatorForm(forms.ModelForm):
    name = forms.RegexField(
        strip=True,
        min_length=2,
        max_length=20,
        regex="^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Aggregator Name",
                "pattern": "^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$",
                "autofocus": True,
            }
        ),
    )

    class Meta:
        model = Aggregator
        fields = ("name",)
