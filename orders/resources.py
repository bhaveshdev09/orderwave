from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields
from import_export.widgets import DateTimeWidget
from orders.models import Bill, Customer


class BillResource(resources.ModelResource):
    bill_id = fields.Field(column_name="Bill No.")
    bill_total = fields.Field(column_name="Total(Rs)")
    customer = fields.Field(
        column_name="Customer",
        attribute="customer",
        widget=ForeignKeyWidget(Customer, field="name"),
    )
    aggregator = fields.Field(
        column_name="Aggregator",
        attribute="aggregator",
        widget=ForeignKeyWidget(Customer, field="name"),
    )
    train_details = fields.Field(
        column_name="Train No/Name",
        attribute="train_details",
    )
    bill_date = fields.Field(
        column_name="DateTime", attribute="bill_date", widget=DateTimeWidget()
    )
    payment_type = fields.Field(column_name="Payment Type", attribute="payment_type")
    order_items = fields.Field(column_name="Order Items")

    class Meta:
        model = Bill
        fields = (
            "bill_id",
            "bill_total",
            "customer",
            "train_details",
            "bill_date",
            "aggregator",
            "payment_type",
            "status",
            "order_items",
        )

    def dehydrate_bill_total(self, object):
        total = getattr(object, "total", 0.0)
        return total

    def dehydrate_bill_id(self, object):
        order_repr = getattr(object, "order_repr", "--not-found--")
        return f"{order_repr}"

    def dehydrate_order_items(self, object):
        order_items_dict = getattr(
            object, "order", "--not-found--"
        ).get_items_for_excel()  #
        return order_items_dict

    # def filter_export(self, queryset, *args, **kwargs):
    #     return super().filter_export(queryset, *args, **kwargs)
