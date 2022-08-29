from converter import result, code_is_valid, num_is_valid, RatesNotAvailableError
from unittest import TestCase

class ConverterTestCase(TestCase):
    def test_valid_number(self):
        """ Determines if input is valid number """
        self.assertTrue(num_is_valid('2'))
        self.asserTrue(num_is_valid('2.0'))
        self.assertTrue(num_is_valid(2))
        self.assertTrue(num_is_valid(2.0))
        self.assertFalse(num_is_valid('two'))
        self.assertFalse(num_is_valid('0'))
        self.assertFalse(num_is_valid(0))
        self.assertFalse(num_is_valid('-2'))
        self.assertFalse(num_is_valid(-2))

    def test_valid_curr_code(self):
        """ Function determines correctly if currency code is a valid code """
        self.assertTrue(code_is_valid('USD'))
        self.assertTrue(code_is_valid('eur'))
        self.assertTrue(code_is_valid('Mxn'))
        self.assertTrue(code_is_valid('GBP'))
        self.assertFalse(code_is_valid('aaa'))
        self.assertFalse(code_is_valid('MEX'))
        self.assertFalse(code_is_valid('a'))
        self.assertFalse(code_is_valid('aaaaaaa'))
        self.assertFalse(code_is_valid('122'))
        self.assertFalse(code_is_valid(12))

    def test_converter(self):
        """ Function returns correct string and handles input values appropriately"""        
        self.assertEqual(result('USD', 'USD', '20'), 'US$20.00')
        self.assertRaises(RatesNotAvailableError, result, 'AAA', 'USD', '20')        
        self.assertEqual(result('USD', 'USD', 20), 'US$20.00')        
        self.assertIn('1.00', result('GBP', 'GBP', '1'))
        self.assertIn('5.10', result('GBP', 'gbp', '5.10'))
        self.assertIsInstance(result('USD', 'USD', '20'), str)