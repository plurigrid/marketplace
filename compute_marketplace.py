```python
import chyp
import hypergraphx
import polars as pl
from utils import validate_data, handle_error

# Constants
COMPUTE_CREDIT_TYPE = 'compute'

# Variables
compute_marketplace = hypergraphx.Hypergraph()

def create_compute_credit(data):
    if not validate_data(data, COMPUTE_CREDIT_TYPE):
        handle_error('Invalid data for compute credit')
        return

    credit_id = chyp.create_credit(COMPUTE_CREDIT_TYPE, data)
    compute_marketplace.add_node(credit_id, data)

    return credit_id

def update_compute_credit(credit_id, data):
    if not validate_data(data, COMPUTE_CREDIT_TYPE):
        handle_error('Invalid data for compute credit')
        return

    chyp.update_credit(credit_id, data)
    compute_marketplace.update_node(credit_id, data)

def delete_compute_credit(credit_id):
    chyp.delete_credit(credit_id)
    compute_marketplace.remove_node(credit_id)

def get_compute_marketplace_state():
    return compute_marketplace.nodes(data=True)

def get_compute_credit(credit_id):
    return compute_marketplace.node[credit_id]
```