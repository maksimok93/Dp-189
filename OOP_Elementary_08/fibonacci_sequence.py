class FibonacciFirstWay:
    """First way of finding fibonacci numbers - using the number of elements in sequence"""

    def __init__(self):
        self.i = 0
        self.fib1 = 0
        self.fib2 = 1
        self.Fib_data = [self.fib1, self.fib2]

    def return_next_number(self):
        """Return next number from Fibonacci numbers list."""
        self.i += 1
        return self.Fib_data[self.i - 1]

    def calculate_fib_number(self, elem_amount):
        """Use previously calculated fibonacci numbers, stored in list Fib_data."""
        length_fib_data = len(self.Fib_data)
        fib1 = self.Fib_data[length_fib_data - 2]
        fib2 = self.Fib_data[length_fib_data - 1]
        new_n = elem_amount - length_fib_data

        for i in range(new_n + 1):
            fib1, fib2 = fib2, fib1 + fib2
            self.Fib_data.append(fib2)
        print(f"Fibonacci sequence with {elem_amount} elements: {self.Fib_data[0:-1]}")


class FibonacciSecondWay:
    """Second way - creating a list of numbers to check for the fibonacci number in the specified range."""

    def __init__(self):
        self.limit1, self.limit2 = (int(num) for num in input("Please, specify range limits using space: ").split())
        self.nums_in_range = []

    def create_range(self):
        """Creating a list of all integer numbers in the specified range."""
        for number in range(self.limit1, self.limit2 + 1):
            self.nums_in_range.append(int(number))
        return self.nums_in_range

    def fib_in_range(self):
        """Output for a fibonacci number in the specified range."""
        print(f"Fibonacci numbers in range {self.limit1}, {self.limit2}:")
        fib1, fib2 = 0, 1
        for elem in range(self.limit1, self.limit2):
            fib1, fib2 = fib2, fib1 + fib2
            if fib1 in self.nums_in_range:
                print(str(fib1), end=' ')


if __name__ == '__main__':
    print(
"""
Choose the search type for fibonacci numbers:
1 - using a number of elements in sequence
2 - using the specified range in which there are Fibonacci numbers
Please, enter 1 or 2:
""")
    while True:
        response = input()
        if response == '1':
            while True:
                elem_amount = int(input("Enter the number of elements in sequence: "))
                if elem_amount > 0:
                    obj = FibonacciFirstWay()
                    obj.calculate_fib_number(elem_amount)
                    break
                else:
                    print("Please enter a positive integer!")

        elif response == '2':
            obj = FibonacciSecondWay()
            obj.create_range()
            obj.fib_in_range()
            break
        else:
            print("Incorrect input! Please, enter 1 or 2: ")
