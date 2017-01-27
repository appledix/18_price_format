import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):

    def test_nothing(self):
        with self.assertRaises(ValueError): format_price()

    def test_int(self):
        self.assertEqual('300 000', format_price(300000))
    
    def test_int_zero(self):
        self.assertEqual('0', format_price(0))
     
    def test_float(self):
        self.assertEqual('1 000.35', format_price(1000.35))

    def test_float_int(self):
        self.assertEqual('1 000', format_price(1000.00))

    def test_float_zero(self):
        self.assertEqual('0', format_price(0.0))

    def test_float_rounding(self):
        self.assertEqual('1 000.36', format_price(1000.355923721361263))    

    def test_string_int(self):
        self.assertEqual('7 668 523', format_price('7668523'))

    def test_string_float_int(self):
        self.assertEqual('76 685', format_price('76685.00'))

    def test_string_float(self):
        self.assertEqual('76 685.23', format_price('76685.23'))

    def test_string_float_with_comma(self):
        self.assertEqual('76 685.23', format_price('76685,23'))

    def test_string_int_zero(self):
        self.assertEqual('0', format_price('0'))

    def test_string_float_zero(self):
        self.assertEqual('0', format_price('0.00'))

    def test_string_ends_with_comma(self):
        self.assertEqual('12 348', format_price('12348,'))

    def test_string_ends_with_dot(self):
        self.assertEqual('12 348', format_price('12348.'))

    def test_negative_int(self):
        with self.assertRaises(ValueError): format_price(-100)

    def test_negative_float(self):
        with self.assertRaises(ValueError): format_price(-50.0)

    def test_negative_string(self):
        with self.assertRaises(ValueError): format_price('-50.0')

    def test_empty_string(self):
        with self.assertRaises(ValueError): format_price('')

    def test_string_with_not_numbers(self):
        with self.assertRaises(ValueError): format_price('31s2abd.e02fg')

    def test_string_with_several_commas(self):
        with self.assertRaises(ValueError): format_price('12,,,348')

    def test_string_with_several_dots(self):
        with self.assertRaises(ValueError): format_price('12...348')


if __name__ == '__main__':
    unittest.main()