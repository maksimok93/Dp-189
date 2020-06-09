from calculation import add, subtract
import unittest
import inspect


class TestFunctions_One_Arg_is_Zero(unittest.TestCase):
    """
    In this class we run two tests ('add' and 'subtract' function from calculation.py module)
    where at least one argument is zero.
    """

    def test_add_zero_arg(self):
        """Test add function if at least one argument is zero."""
        try:
            self.assertEqual(add(0, 23), 23)
        except Exception as error:
            print(error)

    def test_subtract_zero_arg(self):
        """Test subtract function if at least one argument is zero."""
        try:
            self.assertEqual(subtract(0, 30), -30)
        except Exception as error:
            print(error)


class TestFunctions_All_Args_Greater_Zero(unittest.TestCase):
    """
    In this class we run two tests ('add' and 'subtract' function from calculation.py module)
    where all arguments are greater than zero.
    """

    def test_add_all_args_greater_zero(self):
        """Test add function if all arguments are greater than zero."""
        try:
            self.assertEqual(add(17, 23), 40)
        except Exception as error:
            print(error)

    def test_subtract_all_args_greater_zero(self):
        """Test subtract function if all arguments are greater than zero."""
        try:
            self.assertEqual(subtract(30, 16), 15)
        except Exception as error:
            print(f'Got error in {inspect.stack()[0][3]}, {error}')


def getTestSuite():
    """
    Creating two test suites: first suite tests where at least one argument is zero
    and the second suite tests where all arguments are greater than zero.
    """
    suite1 = unittest.makeSuite(TestFunctions_One_Arg_is_Zero)
    suite2 = unittest.makeSuite(TestFunctions_All_Args_Greater_Zero)
    suite = unittest.TestSuite()
    suite.addTest(suite1)
    suite.addTest(suite2)

    runner = unittest.TextTestRunner()
    print(runner.run(suite))


if __name__ == '__main__':
    getTestSuite()
