from pydantic import BaseModel, Field, ValidationError
from decimal import Decimal


class LineItem(BaseModel):
    description: str = Field(max_length=120)
    quantity: int = Field(ge=0, default=1)
    unit_price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)


class Invoice(BaseModel):
    invoice_number: str
    vendor: str
    currency: str = Field(pattern=r"^[A-Z]{3}$", default="GBP")
    line_items: list[LineItem]


raw = {
    "invoice_number": "INV-2026-0988",
    "vendor": "Some fake vendor Ltd",
    "line_items": [
        {"description": "Pallet racking q3", "quantity": "12", "unit_price": "80.5"},
        {"description": "Freight surcharge", "unit_price": "129"},
    ],
}


invoice = Invoice.model_validate(raw)
# print(invoice.line_items[0].quantity)
# print(invoice.model_dump_json(indent=2))

bad = {**raw, "currency": "pounds"}
try:
    Invoice.model_validate(bad)
except ValidationError as e:
    print(e)
    # print(e.errors())
