from django import forms
from purchase_orders.models import PurchaseOrder
from materials.models import Material
from django.db.models import Sum


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ["vendor", "material", "status"]
        widgets = {
            "vendor": forms.Select(attrs={"class": "form-control"}),
            "material": forms.SelectMultiple(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        instance = super(PurchaseOrderForm, self).save(commit=False)

        # Calculate the total price for the selected materials
        total_price = Material.objects.filter(
            id__in=self.cleaned_data["material"]
        ).aggregate(total_price=Sum("price"))["total_price"]
        instance.total = total_price if total_price else 0

        if commit:
            instance.save()
            self.save_m2m()

        return instance
