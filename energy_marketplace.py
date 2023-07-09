```python
import chyp
import hypergraphx
import polars as pl
from utils import validate_data, handle_error

# Constants
ENERGY_CREDIT_SCHEMA = {
    "id": "string",
    "amount": "int",
    "price": "float",
    "seller_id": "string",
    "buyer_id": "string"
}

# Variables
energy_marketplace = pl.DataFrame([], columns=list(ENERGY_CREDIT_SCHEMA.keys()))

def create_energy_credit(data):
    if not validate_data(data, ENERGY_CREDIT_SCHEMA):
        handle_error("Invalid data format for energy credit")
        return

    global energy_marketplace
    energy_marketplace = energy_marketplace.with_row(data)

def update_energy_credit(credit_id, data):
    global energy_marketplace
    if credit_id not in energy_marketplace["id"]:
        handle_error("Energy credit not found")
        return

    if not validate_data(data, ENERGY_CREDIT_SCHEMA, partial=True):
        handle_error("Invalid data format for energy credit")
        return

    energy_marketplace = energy_marketplace.update(data, where=(pl.col("id") == credit_id))

def delete_energy_credit(credit_id):
    global energy_marketplace
    if credit_id not in energy_marketplace["id"]:
        handle_error("Energy credit not found")
        return

    energy_marketplace = energy_marketplace.filter(pl.col("id") != credit_id)

def get_energy_marketplace():
    return energy_marketplace
```