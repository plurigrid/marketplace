```python
import unittest
from src.compute import Compute, exchange_compute

class TestCompute(unittest.TestCase):

    def setUp(self):
        self.compute1 = Compute(100)
        self.compute2 = Compute(200)

    def test_compute_creation(self):
        self.assertEqual(self.compute1.credits, 100)
        self.assertEqual(self.compute2.credits, 200)

    def test_exchange_compute(self):
        exchange_compute(self.compute1, self.compute2, 50)
        self.assertEqual(self.compute1.credits, 50)
        self.assertEqual(self.compute2.credits, 250)

    def test_exchange_compute_failure(self):
        with self.assertRaises(ValueError):
            exchange_compute(self.compute1, self.compute2, 150)

    def tearDown(self):
        self.compute1 = None
        self.compute2 = None

if __name__ == '__main__':
    unittest.main()
```