from django import forms
from purchase_orders.models import PurchaseOrder, PurchaseOrderItem
from materials.models import Material
from vendors.models import Vendor
from django.db.models import Sum
from django.forms import inlineformset_factory


class PurchaseOrderItemForm(forms.ModelForm):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control item-qty",
                "min": "1",
                "value": "1",
                "required": True,
            }
        ),
        min_value=1,
    )

    class Meta:
        model = PurchaseOrderItem
        fields = ["material", "quantity"]
        widgets = {
            "material": forms.Select(
                attrs={"class": "form-select item-select", "required": True}
            ),
        }


PurchaseOrderItemFormSet = inlineformset_factory(
    PurchaseOrder,
    PurchaseOrderItem,
    form=PurchaseOrderItemForm,
    min_num=1,
    can_delete=True,
    extra=0,
)


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ["vendor", "status"]
        widgets = {
            "vendor": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }

    # Include fields for customer details
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.purchase_orderitem_formset = PurchaseOrderItemFormSet(
            prefix="purchase_order_items"
        )

        try:
            if self.instance is not None:
                self.purchase_orderitem_formset = PurchaseOrderItemFormSet(
                    instance=self.instance, prefix="purchase_order_items"
                )

        except Exception as e:
            pass

    def is_valid(self):
        return True

    def save(self, commit=True):
        self.cleaned_data = self.data

        if not self.instance:
            self.instance = PurchaseOrder.objects.create(self.cleaned_data)
        else:
            self.instance.status = self.cleaned_data["status"]
            self.instance.vendor = Vendor.objects.get(id=self.cleaned_data["vendor"])
            self.instance.save()

        self.purchase_orderitem_formset = PurchaseOrderItemFormSet(
            self.cleaned_data, instance=self.instance, prefix="purchase_order_items"
        )

        if self.purchase_orderitem_formset.is_valid():
            self.purchase_orderitem_formset.save()

        return self.instance
