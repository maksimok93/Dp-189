"""After the user enters a number, the program displays its text version.
For example: 312 - three hundred twelve."""


def convert_to_word(number):
    """Depending on the length of the number a function from a specific lists
    (units, tens, hundreds, etc.) in order finds each word corresponding to its
    number in the list."""
    ones = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven', 'eight ', 'nine ']
    tens = ['ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ',
            'nineteen ']
    decades = ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy', 'eighty ', 'ninety ']
    hundreds = ['', 'one hundred ', 'two hundred ', 'three hundred ', 'four hundred ', 'five hundred ', 'six hundred ',
                'seven hundred ', 'eight hundred ', 'nine hundred ']
    large_nums = ['thousand, ', 'million, ', 'billion, ', 'trillion, ']

    word = ''
    length = len(number)
    up_length = 0

    while length > 0:
        if number == '0':
            word = 'zero'
            break
        elif length > 1 and number[length - 2] == '1':
            for i in range(0, 10):
                if number[length - 1] == str(i):
                    word = tens[i] + word
        else:
            for i in range(0, 10):
                if number[length - 1] == str(i):
                    word = ones[i] + word
            if length > 1:
                for i in range(0, 10):
                    if number[length - 2] == str(i):
                        word = decades[i] + word
        if length > 2:
            for i in range(0, 10):
                if number[length - 3] == str(i):
                    word = hundreds[i] + word
        if length > 3:
            word = large_nums[up_length] + word
        length = length - 3
        up_length += 1

    print(word)


if __name__ == '__main__':
    while True:
        number = input('Type any number here: ')
        while not (number.isdigit()):
            print('Only numbers are allowed!')
            number = input('Type any number here: ')
        convert_to_word(number)
        response = input('Would you like to enter another number (Yes / No)? ').lower()
        if response != 'yes' and response != 'y':
            break
