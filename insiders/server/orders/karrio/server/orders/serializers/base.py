from enum import Enum
from rest_framework import fields
from karrio.server.core.serializers import (
    Address,
    AddressData,
    Commodity,
    CommodityData,
    PlainDictField,
    Serializer,
    EntitySerializer,
    Shipment,
    allow_model_id,
    valid_date_format,
)


class OrderStatus(Enum):
    unfulfilled = "unfulfilled"
    cancelled = "cancelled"
    fulfilled = "fulfilled"
    delivered = "delivered"
    partial = "partial"


ORDER_STATUS = [(c.value, c.value) for c in list(OrderStatus)]


@allow_model_id(
    [
        ("shipping_to", "karrio.server.manager.models.Address"),
        ("shipping_from", "karrio.server.manager.models.Address"),
        ("line_items", "karrio.server.manager.models.Commodity"),
    ]
)
class OrderData(Serializer):
    order_id = fields.CharField(required=True, help_text="The source' order id.")
    order_date = fields.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        validators=[valid_date_format("order_date")],
        help_text="The order date. format: `YYYY-MM-DD`",
    )
    source = fields.CharField(
        required=False,
        default="API",
        help_text="""
    The order's source.

    e.g. API, POS, ERP, Shopify, Woocommerce, etc.
    """,
    )
    shipping_to = AddressData(
        required=True,
        help_text="The customer or recipient address for the order.",
    )
    shipping_from = AddressData(
        required=False,
        allow_null=True,
        help_text="The origin or warehouse address of the order items.",
    )
    line_items = CommodityData(
        many=True, allow_empty=False, help_text="The order line items."
    )
    options = PlainDictField(
        required=False,
        allow_null=True,
        help_text="""
    <details>
    <summary>The options available for the order shipments.</summary>

    ```
    {
        "currency": "USD",
        "paid_by": "third_party",
        "payment_account_number": "123456789",
        "duty_paid_by": "third_party",
        "duty_account_number": "123456789",
        "invoice_number": "123456789",
        "invoice_date": "2020-01-01",
        "single_item_per_parcel": true,
        "carrier_ids": ["canadapost-test"],
    }
    ```

    Please check the docs for shipment specific options.
    </details>
    """,
    )
    metadata = PlainDictField(
        required=False, default={}, help_text="User metadata for the order."
    )


class LineItem(Commodity):
    unfulfilled_quantity = fields.IntegerField(default=0)


class Order(EntitySerializer):
    object_type = fields.CharField(
        default="order", help_text="Specifies the object type"
    )
    order_id = fields.CharField(required=True, help_text="The source' order id.")
    order_date = fields.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        validators=[valid_date_format("order_date")],
        help_text="The order date. format: `YYYY-MM-DD`",
    )
    source = fields.CharField(required=False, help_text="The order's source.")
    status = fields.ChoiceField(
        choices=ORDER_STATUS,
        default=OrderStatus.unfulfilled.value,
        help_text="The order status.",
    )
    shipping_to = Address(
        required=True,
        help_text="The customer address for the order.",
    )
    shipping_from = Address(
        required=False,
        allow_null=True,
        help_text="The origin or warehouse address of the order items.",
    )
    line_items = LineItem(
        many=True, allow_empty=False, help_text="The order line items."
    )
    options = PlainDictField(
        required=False,
        allow_null=True,
        help_text="""
    <details>
    <summary>The options available for the order shipments.</summary>

    ```
    {
        "currency": "USD",
        "paid_by": "third_party",
        "payment_account_number": "123456789",
        "duty_paid_by": "third_party",
        "duty_account_number": "123456789",
        "invoice_number": "123456789",
        "invoice_date": "2020-01-01",
        "single_item_per_parcel": true,
        "carrier_ids": ["canadapost-test"],
    }
    ```

    Please check the docs for shipment specific options.
    </details>
    """,
    )
    metadata = PlainDictField(
        required=False, default={}, help_text="User metadata for the order."
    )
    shipments = Shipment(
        many=True,
        required=False,
        help_text="The shipments associated with the order.",
    )
    test_mode = fields.BooleanField(
        required=True,
        help_text="Specify whether the order is in test mode or not.",
    )
    created_at = fields.CharField(
        required=True,
        help_text="""
    The shipment creation datetime

    Date Format: `YYYY-MM-DD HH:MM:SS.mmmmmmz`
    """,
    )
