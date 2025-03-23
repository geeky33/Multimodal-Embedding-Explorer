import unittest
from src.data_loader import load_data

class TestApp(unittest.TestCase):
    def test_load_data(self):
        data = load_data('dataset/pmd_sample.csv')
        self.assertIsNotNone(data)