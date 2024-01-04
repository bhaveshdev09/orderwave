from django import forms
from aggregators.models import Aggregator


class AggregatorForm(forms.ModelForm):
    name = forms.CharField(strip=True, min_length=2, max_length=20)

    class Meta:
        model = Aggregator
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Aggregator Name"}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")

        # Check if the name contains only alphabets
        if not name.isalpha():
            raise forms.ValidationError("Aggregator name should contain only alphabets.")

        return name
