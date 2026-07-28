from pydantic import BaseModel, Field, ValidationError


class Product(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)
    in_stock: bool = True


raw_data = {"name": "Laptop", "price": "999.99"}

product = Product(**raw_data)

# print(product)

json_data = '{"name":"Mobile Phone","price":"1","in_stock":"no"}'

try:
    Product.model_validate_json(json_data)
except ValidationError as e:
    print(e.errors())
