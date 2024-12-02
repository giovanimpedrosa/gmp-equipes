from datetime import datetime
from django.test import TestCase

# Create your tests here.
from core.utils.date_utils import date_to_str, str_to_date
from core.utils.decimal_utils import str_to_decimal

class TestDateUtils(TestCase):
    def test_str_to_date(self):
        self.assertEqual(str_to_date("2024-12-01"), datetime(2024, 12, 1))

    def test_date_to_str(self):
        self.assertEqual(date_to_str(datetime(2024, 12, 1)), "2024-12-01")        

    def test_str_to_decimal(self):
        self.assertEqual(str_to_decimal("125.845.666,99"), str_to_decimal('125845666,99'))                