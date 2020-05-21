"""
Each number in the Fibonacci sequence is the sum of the two numbers that precede it.
So, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on. In this program,
we can choose two ways of finding numbers - using the number of elements in sequence
or using specified range of numbers in which there can be fibonacci numbers.
"""

def fib_formula(n):
    """First way of finding fibonacci numbers - calculation formula."""
    if n <= 1:
        return n
    else:
        return (fib_formula(n - 1) + fib_formula(n - 2))


def output_elem():
    """Sequence output according to the length of the sequence."""
    while True:
        n_elements = int(input("Enter the number of elements in sequence: "))
        if n_elements > 0:
            print("Fibonacci sequence: ", [fib_formula(elem) for elem in range(n_elements)])
            break
        else:
            print(" Please enter a positive integer! ")


def create_range():
    """Second way - creating a list of numbers to check for the fibonacci number in the specified range."""
    limit1, limit2 = (int(num) for num in input("Please, specify range limits using space: ").split())
    nums_in_range = []
    for _ in range(limit1, limit2 + 1):
        nums_in_range.append(int(_))
    return limit1, limit2, nums_in_range


def fib_in_range():
    """Output for a number in the range."""
    limit1, limit2, nums_in_range = create_range()
    fib1, fib2 = 0, 1
    for elem in range(limit1, limit2):
        fib1, fib2 = fib2, fib1 + fib2
        if fib1 in nums_in_range:
            print(fib1)


if __name__ == '__main__':
    print("""Choose the type of search for fibonacci numbers:
1 - using input a number of elements in sequence
2 - using the specified range in which there are Fibonacci numbers
Please, enter 1 or 2: """)

    while True:
        response = input()
        if response == '1':
            output_elem()
            break
        elif response == '2':
            fib_in_range()
            break
        else:
            print("Incorrect input! Please, enter 1 or 2: ")
