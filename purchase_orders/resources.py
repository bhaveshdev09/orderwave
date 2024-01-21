from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields
from import_export.widgets import DateTimeWidget
from purchase_orders.models import PurchaseOrder, Vendor


class PurchaseOrderResource(resources.ModelResource):
    po_id = fields.Field(column_name="Purchase Order No.")
    po_total = fields.Field(column_name="Total(Rs)")
    vendor = fields.Field(
        column_name="Vendor",
        attribute="vendor",
        widget=ForeignKeyWidget(Vendor, field="name"),
    )
    po_date = fields.Field(
        column_name="DateTime", attribute="order_date", widget=DateTimeWidget(format="")
    )
    po_items = fields.Field(column_name="Order Items [(Item, Quantity, Total)]")

    class Meta:
        model = PurchaseOrder
        fields = (
            "po_id",
            "po_total",
            "vendor",
            "po_date",
            "status",
            "po_items",
        )

    def dehydrate_po_total(self, object):
        total = getattr(object, "total_cost", 0.0)
        return total

    def dehydrate_po_id(self, object):
        order_repr = getattr(object, "purchase_order_id", "--not-found--")
        return f"{order_repr}"

    def dehydrate_po_items(self, object):
        order_items_dict = object.get_items_for_excel()  #
        return order_items_dict

    # def filter_export(self, queryset, *args, **kwargs):
    #     return super().filter_export(queryset, *args, **kwargs)
