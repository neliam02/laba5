import unittest
from src.sponsor import Sponsor

class TestSponsor(unittest.TestCase):
    def test_initialization(self):
        sponsor = Sponsor("BrandX", 5000)
        self.assertEqual(sponsor.name, "BrandX")
        self.assertEqual(sponsor.budget, 5000)

if __name__ == "__main__":
    unittest.main()
