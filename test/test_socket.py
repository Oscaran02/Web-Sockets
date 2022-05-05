import unittest
import app

class TestSocket(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(app.is_prime(2))
        self.assertTrue(app.is_prime(3))
        self.assertTrue(app.is_prime(5))
        self.assertTrue(app.is_prime(7))
        self.assertTrue(app.is_prime(11))
        self.assertFalse(app.is_prime(4))
        self.assertFalse(app.is_prime(6))
        self.assertFalse(app.is_prime(8))
        self.assertFalse(app.is_prime(9))
        self.assertFalse(app.is_prime(10))

    def test_is_even(self):
        self.assertTrue(app.is_even(2))
        self.assertFalse(app.is_even(3))
        self.assertTrue(app.is_even(4))
        self.assertFalse(app.is_even(5))
        self.assertTrue(app.is_even(6))
        self.assertFalse(app.is_even(7))
        self.assertTrue(app.is_even(8))
        self.assertFalse(app.is_even(9))
        self.assertTrue(app.is_even(10))

    def test_data_block(self):
        data_block = app.DataBlock()
        data_block.update_data(2)
        data_block.update_data(3)
        data_block.update_data(5)
        data_block.update_data(7)
        data_block.update_data(11)
        data_block.update_data(4)
        data_block.update_data(6)
        data_block.update_data(8)
        data_block.update_data(9)
        data_block.update_data(10)
        self.assertEqual(data_block.get_max_number(), 11)
        self.assertEqual(data_block.get_min_number(), 2)
        self.assertEqual(data_block.get_first_number(), 2)
        self.assertEqual(data_block.get_last_number(), 10)
        self.assertEqual(data_block.get_number_of_prime_numbers(), 5)
        self.assertEqual(data_block.get_number_of_even_numbers(), 5)
        self.assertEqual(data_block.get_number_of_odd_numbers(), 5)

    def


if __name__ == '__main__':
    unittest.main()
