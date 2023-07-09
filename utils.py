```python
import chyp
import hypergraphx
import polars as pl

# Constants
MARKETPLACE_NAMES = ['energy', 'services', 'compute']
CREDIT_TYPES = ['energy_credits', 'service_credits', 'compute_credits']

# Data Schemas
energy_schema = pl.DataFrame({
    'credit_id': pl.Series([], dtype=pl.Int64),
    'credit_value': pl.Series([], dtype=pl.Float64),
    'credit_owner': pl.Series([], dtype=pl.str)
})

service_schema = pl.DataFrame({
    'credit_id': pl.Series([], dtype=pl.Int64),
    'credit_value': pl.Series([], dtype=pl.Float64),
    'credit_owner': pl.Series([], dtype=pl.str),
    'service_type': pl.Series([], dtype=pl.str)
})

compute_schema = pl.DataFrame({
    'credit_id': pl.Series([], dtype=pl.Int64),
    'credit_value': pl.Series([], dtype=pl.Float64),
    'credit_owner': pl.Series([], dtype=pl.str),
    'compute_type': pl.Series([], dtype=pl.str)
})

# Utility Functions
def validate_data(data, schema):
    try:
        data = pl.DataFrame(data)
        assert data.frame_equal(schema)
        return True
    except AssertionError:
        return False

def handle_error(error):
    print(f"An error occurred: {error}")

def create_message(message_type, marketplace, credit_id=None):
    messages = {
        'transaction_success': f"Transaction successful in {marketplace} marketplace.",
        'transaction_error': f"Transaction failed in {marketplace} marketplace.",
        'update_success': f"Update successful in {marketplace} marketplace.",
        'update_error': f"Update failed in {marketplace} marketplace.",
        'delete_success': f"Deletion successful in {marketplace} marketplace.",
        'delete_error': f"Deletion failed in {marketplace} marketplace."
    }
    if credit_id:
        return messages[message_type] + f" Credit ID: {credit_id}"
    else:
        return messages[message_type]
```