```python
import matplotlib.pyplot as plt
from hypergraphx import Hypergraph

class StringDiagram:
    def __init__(self, hypergraph: Hypergraph):
        self.hypergraph = hypergraph

    def generate_string_diagram(self):
        plt.figure(figsize=(10, 10))
        plt.title('String Diagram of Energy Credit Marketplace')
        self.hypergraph.draw()
        plt.show()

    def save_string_diagram(self, filename: str):
        plt.figure(figsize=(10, 10))
        plt.title('String Diagram of Energy Credit Marketplace')
        self.hypergraph.draw()
        plt.savefig(filename)
```