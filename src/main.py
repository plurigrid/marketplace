```python
import sys
from energy_marketplace import EnergyMarketplace
from services import Services
from compute import Compute
from visualization import Visualization
from hypergraph import Hypergraph
from string_diagrams import StringDiagram

def main():
    # Initialize the marketplace, services, compute, visualization, hypergraph, and string diagrams
    marketplace = EnergyMarketplace()
    services = Services()
    compute = Compute()
    visualization = Visualization()
    hypergraph = Hypergraph()
    string_diagram = StringDiagram()

    # Exchange energy, services, and compute
    exchange_energy_status = marketplace.exchange_energy()
    exchange_services_status = services.exchange_services()
    exchange_compute_status = compute.exchange_compute()

    # Check if the exchanges were successful
    if exchange_energy_status == 'EXCHANGE_SUCCESS' and exchange_services_status == 'EXCHANGE_SUCCESS' and exchange_compute_status == 'EXCHANGE_SUCCESS':
        print("All exchanges were successful.")
    else:
        print("One or more exchanges failed.")
        sys.exit(1)

    # Visualize the hypergraph and generate the string diagram
    visualize_hypergraph_status = visualization.visualize_hypergraph(hypergraph)
    generate_string_diagram_status = string_diagram.generate_string_diagram(hypergraph)

    # Check if the visualizations were successful
    if visualize_hypergraph_status == 'VISUALIZATION_SUCCESS' and generate_string_diagram_status == 'VISUALIZATION_SUCCESS':
        print("All visualizations were successful.")
    else:
        print("One or more visualizations failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```