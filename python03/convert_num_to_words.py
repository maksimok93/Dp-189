"""This module imports num2words library from pypi and executes and starts conversion."""
from num2words import num2words


def convert_num_into_word():
    """Program asks the user for a number and displays the word corresponding to the number."""
    print(num2words(input("Hello, my friend! \nPlease, enter a number: ")))
