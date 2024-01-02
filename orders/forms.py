# forms.py
from django import forms
from django.forms import inlineformset_factory
from orders.models import Order, OrderItem, Bill
from customers.models import Customer
from customers.forms import CustomerForm
from items.models import Item


class OrderItemForm(forms.ModelForm):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control item-qty", "min": "1"}),
        min_value=1,
    )

    class Meta:
        model = OrderItem
        fields = ["item", "quantity"]
        widgets = {
            "item": forms.Select(attrs={"class": "form-control item-select"}),
        }


OrderItemFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm, min_num=1, can_delete=True, extra=0
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["discount"]
        widgets = {
            "discount": forms.NumberInput(attrs={"class": "form-control"}),
        }

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


# class BillForm(forms.ModelForm):
#     train_name = forms.CharField(required=False)
#     train_no = forms.CharField(required=False)

#     class Meta:
#         model = Bill
#         exclude = "__all__"

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.customer_form = CustomerForm(*args, **kwargs)
#         self.orderitem_formset = OrderItemFormSet(*args, **kwargs)

#     def is_valid(self):
#         print(self.customer_form.data)
#         return (
#             super().is_valid()
#             and self.customer_form.is_valid()
#             and self.orderitem_formset.is_valid()
#         )

#     def save(self, commit=True):
#         customer = self.customer_form.cleaned_data
#         order_items = self.orderitem_formset.cleaned_data

#         print(f"{order_items=}")
#         # Create Customer instance
#         customer_instance = Customer.objects.create(
#             name=customer["name"], email=customer["email"], mobile=customer["mobile"]
#         )

#         # Create Order instance
#         order_instance = Order.objects.create(customer=customer_instance)

#         # Create OrderItem instances
#         for item in order_items:
#             OrderItem.objects.create(
#                 item=item["item"], quantity=item["quantity"], order=order_instance
#             )

#         # Create Bill instance
#         bill_instance = super().save(commit=False)
#         bill_instance.order = order_instance
#         bill_instance.save()

#         return bill_instance


# OrderItemFormSet = inlineformset_factory(
#     Bill, OrderItem, form=OrderItemForm, extra=1, can_delete=False
# )

# OrderItemFormSet = inlineformset_factory(Bill, OrderItem, form=OrderItemForm, extra=1, can_delete=False)


class BillForm(forms.ModelForm):
    train_name = forms.CharField(required=False)
    train_number = forms.CharField(required=False)

    class Meta:
        model = Bill
        fields = ["train_number", "train_name", "status"]
        widgets = {"status": forms.Select(attrs={"class": "form-control"})}

    # Include fields for customer details
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer_form = CustomerForm()
        self.orderform = OrderForm()
        self.orderitem_formset = OrderItemFormSet(prefix="orderitems")
        self.order_instance = None

        try:
            if self.instance is not None:
                self.customer_form = CustomerForm(instance=self.instance.customer)
                self.orderform = OrderForm(instance=self.instance.order)
                self.orderitem_formset = OrderItemFormSet(
                    instance=self.instance.order, prefix="orderitems"
                )

                self.order_instance = self.instance.order
        except Exception as e:
            pass
        # self.customer_form = CustomerForm(instance=self.instance.customer)
        # self.orderform = OrderForm()
        # self.orderitem_formset = OrderItemFormSet()
        # if self.instance:
        #     print(self.instance)
        #     self.customer_form = CustomerForm(instance=self.instance.customer)
        #     self.orderform = OrderForm(instance=self.instance.order)
        #     self.orderitem_formset = OrderItemFormSet(instance=self.instance.order)

    def is_valid(self):
        # print(self.orderitem_formset.is_valid())
        # return super().is_valid() and self.customer_form.is_valid()
        return True

    def save(self, commit=True):
        self.cleaned_data = self.data

        # Create Customer instance
        customer_instance, created = Customer.objects.get_or_create(
            name=self.cleaned_data["name"],
            email=self.cleaned_data["email"],
            mobile=self.cleaned_data["mobile"],
        )

        # Create Order instance
        if not self.order_instance:
            self.order_instance = Order.objects.create()

        order_formset = OrderItemFormSet(
            self.data, instance=self.order_instance, prefix="orderitems"
        )

        if order_formset.is_valid():
            order_formset.save()

        # Create Bill instance
        bill_instance, created = Bill.objects.get_or_create(
            train_name=self.cleaned_data["train_name"],
            train_number=self.cleaned_data["train_number"],
            status=Bill.STATUS_CHOICE_PENDING,
            order=self.order_instance,
            customer=customer_instance,
        )

        return bill_instance
