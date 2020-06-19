"""
The program works in two modes:
1. Count the number of occurrences of a string in a text file in next format:
<Path to the text file>, <Line for counting>
2. Replace a specified string with another in a text file in next format:
<Path to the text file>, <search string>, <replacement string>
"""


class FileManager:
    """FileManager helps in opening a file, writing/reading contents and then closing it."""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


class LineCounter:
    """This class counts the number of occurrences of a string in a text file."""

    def __init__(self, counter):
        self.counter = counter
        self.search_string = search_string

    def get_line_occurrence(self, path) -> str:
        """Counting occurrences of a string in a specified text file."""
        self.counter = 0
        with FileManager(path, 'r') as file:
            contents = file.read().splitlines()
            for line in contents:
                if self.search_string in line:
                    self.counter += 1
        return f"Total number of occurrence of line is: {self.counter}"


class ReplaceLine:
    """This class replaces a specified string with another in the text file."""

    def __init__(self, counter):
        self.counter = counter
        self.search_string = search_string
        self.replace_string = replace_string

    def find_replace(self, path):
        """Finding and replacing the specified string."""
        with FileManager(path, 'r') as file:
            contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
        with FileManager(path, 'w') as file:
            file.write(contents)


if __name__ == '__main__':
    while True:
        user_input = input("Please, write down 2 or 3 parameters as described above using comma: ").split(', ')

        if len(user_input) == 2:
            path = user_input[0]
            search_string = user_input[1]
            line_counter = LineCounter(path)
            print(line_counter.get_line_occurrence(path))

            response = input('Would you like to run the program again (Yes / No)? ').lower()
            if response != 'yes' and response != 'y':
                break

        elif len(user_input) == 3:
            path = user_input[0]
            search_string = user_input[1]
            replace_string = user_input[2]
            replace = ReplaceLine(path)
            replace.find_replace(path)
            print("The specified string was successfully replaced.")

            response = input('Would you like to run the program again (Yes / No)? ').lower()
            if response != 'yes' and response != 'y':
                break

        else:
            print('Please, enter the correct input! ')
