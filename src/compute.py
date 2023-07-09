```python
import chyp
from hypergraphx import Hypergraph
from polars import DataFrame

from src.hypergraph import Hypergraph
from src.energy_marketplace import Energy

class Compute:
    def __init__(self, hypergraph: Hypergraph):
        self.hypergraph = hypergraph

    def exchange_compute(self, energy: Energy, compute_units: int):
        if energy.units < compute_units:
            return 'EXCHANGE_FAILURE'

        self.hypergraph.add_edge(energy, compute_units)
        energy.units -= compute_units

        return 'EXCHANGE_SUCCESS'

    def visualize_hypergraph(self):
        self.hypergraph.draw()

    def generate_string_diagram(self):
        df = DataFrame({
            'source': [edge[0] for edge in self.hypergraph.edges()],
            'target': [edge[1] for edge in self.hypergraph.edges()],
            'value': [edge[2]['weight'] for edge in self.hypergraph.edges()]
        })

        return chyp.plot(df, source='source', target='target', value='value')
```