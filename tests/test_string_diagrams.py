```python
import unittest
from src.string_diagrams import StringDiagram

class TestStringDiagrams(unittest.TestCase):

    def setUp(self):
        self.string_diagram = StringDiagram()

    def test_generate_string_diagram(self):
        result = self.string_diagram.generate_string_diagram()
        self.assertIsNotNone(result, "Failed to generate string diagram")

    def test_visualize_hypergraph(self):
        result = self.string_diagram.visualize_hypergraph()
        self.assertIsNotNone(result, "Failed to visualize hypergraph")

    def tearDown(self):
        self.string_diagram = None

if __name__ == '__main__':
    unittest.main()
```