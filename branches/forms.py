from django import forms
from branches.models import Branch


class BranchForm(forms.ModelForm):
    name = forms.CharField(strip=True, min_length=2, max_length=20)

    class Meta:
        model = Branch
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Branch Name"}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")

        # Check if the name contains only alphabets
        if not name.isalpha():
            raise forms.ValidationError("Branch name should contain only alphabets.")

        return name
