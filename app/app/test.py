
from django.test import SimpleTestCase
from .calc import add

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """ Testing add two numbers"""
        res =  add(3,5)
        self.assertEqual(res,8)
    