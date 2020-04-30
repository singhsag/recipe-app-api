from django.test import TestCase
from app.calc import add, sub


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers add"""
        self.assertEqual(add(2, 14), 16)

    def test_sub_numbers(self):
        """Test that two numbers substracy"""
        self.assertEqual(sub(2, 14), 12)
