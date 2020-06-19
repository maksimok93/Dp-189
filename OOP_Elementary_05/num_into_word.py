"""The program converts the entered integer into a word like this: 12 - twelve."""


class DataOfWords:
    """Instances of this class are word lists according to their category of numbers."""

    def __init__(self):
        self.ones = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven', 'eight ', 'nine ']
        self.tens = ['ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ',
                     'eighteen ', 'nineteen ']
        self.decades = ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy', 'eighty ', 'ninety ']
        self.hundreds = ['', 'one hundred ', 'two hundred ', 'three hundred ', 'four hundred ', 'five hundred ',
                         'six hundred ', 'seven hundred ', 'eight hundred ', 'nine hundred ']
        self.large_nums = ['thousand, ', 'million, ', 'billion, ', 'trillion, ']
        self.length = len(entered_number)
        self.up_length = 0

    def convert(self, entered_number):
        word = ''
        while self.length > 0:
            if entered_number == '0':
                word = 'zero'
                break
            elif self.length > 1 and entered_number[self.length - 2] == '1':
                for i in range(0, 10):
                    if entered_number[self.length - 1] == str(i):
                        word = self.tens[i] + word
            else:
                for i in range(0, 10):
                    if entered_number[self.length - 1] == str(i):
                        word = self.ones[i] + word
                if self.length > 1:
                    for i in range(0, 10):
                        if entered_number[self.length - 2] == str(i):
                            word = self.decades[i] + word
            if self.length > 2:
                for i in range(0, 10):
                    if entered_number[self.length - 3] == str(i):
                        word = self.hundreds[i] + word
            if self.length > 3:
                word = self.large_nums[self.up_length] + word
            self.length = self.length - 3
            self.up_length += 1

        print(word)


if __name__ == '__main__':
    while True:
        entered_number = input('Type any number here: ')
        while not entered_number.isdigit():
            print('Only positive integers are allowed!')
            entered_number = input('Type any number here: ')

        convert_to_word = DataOfWords()
        convert_to_word.convert(entered_number)

        response = input('Would you like to enter another number (Yes / No)? ').lower()
        if response != 'yes' and response != 'y':
            break
