from calculation import add, subtract
import unittest
import inspect


class TestAddFunction(unittest.TestCase):
    """Test add function from calculation.py module."""

    def test_add_all_args_greater_zero(self):
        """Test add function if all arguments are greater than zero."""
        try:
            self.assertEqual(add(17, 23), 40)
        except Exception as error:
            print(error)

    def test_add_all_args_less_zero(self):
        """Test add function if all arguments are less than zero."""
        try:
            self.assertEqual(add(-7, -11), -18)
        except Exception as error:
            print(error)

    def test_add_zero_arg(self):
        """Test add function if at least one argument is zero."""
        try:
            self.assertEqual(add(0, 15), 15)
        except Exception as error:
            print(error)


class TestSubtractFunction(unittest.TestCase):
    """Test subtract function from calculation.py module."""

    def test_subtract_all_args_greater_zero(self):
        """Test subtract function if all arguments are greater than zero."""
        try:
            self.assertEqual(subtract(30, 16), 15)
        except Exception as error:
            print(f'Got error in {inspect.stack()[0][3]}, {error}')

    def test_subtract_all_args_less_zero(self):
        """Test subtract function if all arguments are less than zero."""
        try:
            self.assertEqual(subtract(-18, -5), -13)
        except Exception as error:
            print(error)

    def test_subtract_zero_arg(self):
        """Test subtract function if at least one argument is zero."""
        try:
            self.assertEqual(subtract(0, -6), 7)
        except Exception as error:
            print(f'Got error in {inspect.stack()[0][3]}, {error}')


if __name__ == '__main__':
    unittest.main()
