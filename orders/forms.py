# forms.py
from django import forms
from django.forms import inlineformset_factory
from orders.models import Order, OrderItem
from items.models import Item


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["item", "quantity"]


OrderItemFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm, extra=1, can_delete=True
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["discount"]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.orderitem_formset = OrderItemFormSet(
            instance=self.instance, prefix="orderitems"
        )

    # TODO: Not Configured Properly, Learn
    def is_valid(self):
        return True

    def save(self, commit=True):
        instance = super(OrderForm, self).save(commit)
        data_item_list = self.data.getlist("orderitems-0-item")
        data_item_qty_list = self.data.getlist("orderitems-0-quantity")
        for each in zip(data_item_list, data_item_qty_list):
            data = {
                "item": Item.objects.get(id=int(each[0])),
                "quantity": int(each[1]),
            }
            orderitem = OrderItem.objects.create(
                **data,
                order=instance,
            )

        return instance
