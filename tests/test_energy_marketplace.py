```python
import unittest
from src.energy_marketplace import EnergyMarketplace, Energy

class TestEnergyMarketplace(unittest.TestCase):

    def setUp(self):
        self.marketplace = EnergyMarketplace()
        self.energy = Energy(100, 'solar')

    def tearDown(self):
        self.marketplace = None
        self.energy = None

    def test_exchange_energy(self):
        initial_energy_count = len(self.marketplace.energy_list)
        self.marketplace.exchange_energy(self.energy)
        self.assertEqual(len(self.marketplace.energy_list), initial_energy_count + 1)

    def test_exchange_energy_failure(self):
        self.energy.amount = 0
        response = self.marketplace.exchange_energy(self.energy)
        self.assertEqual(response, 'EXCHANGE_FAILURE')

    def test_visualize_hypergraph(self):
        self.marketplace.exchange_energy(self.energy)
        response = self.marketplace.visualize_hypergraph()
        self.assertEqual(response, 'VISUALIZATION_SUCCESS')

    def test_visualize_hypergraph_failure(self):
        response = self.marketplace.visualize_hypergraph()
        self.assertEqual(response, 'VISUALIZATION_FAILURE')

if __name__ == '__main__':
    unittest.main()
```