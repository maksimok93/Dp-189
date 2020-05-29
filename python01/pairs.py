def create_list(*args) -> list:
    """Creating a list of entered numbers"""
    num = input("Enter the numbers: ").split()
    entered_numbers = []
    for _ in num:
        entered_numbers.append(int(_))
    return entered_numbers


def iterate_all_pairs():
    """Iterate over all possible pairs of numbers in the generated list"""
    entered_numbers = create_list()
    pairs = []
    for arg1 in entered_numbers:
        for arg2 in entered_numbers:
            if arg2 >= arg1 and (arg2 + arg1) == 10:
                pairs.append(f'{arg1} + {arg2}')
    distinct_pairs = set(pairs)
    for pair in distinct_pairs:
        print(pair)


if __name__ == '__main__':
    iterate_all_pairs()