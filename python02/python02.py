class FileStatistic:
    @staticmethod
    def total_lines(file):
        """Counting the number of all lines in a file."""
        total_line = 0
        for line in file:
            total_line += 1
        return total_line

    @staticmethod
    def number_of_empty_lines(file):
        """Counting empty lines."""
        empty_line = 0
        for line in file:
            if len(line) == 1:
                empty_line += 1
        return empty_line

    @staticmethod
    def lines_with_z(file):
        """Output the number of lines with 'z'."""
        z_line = 0
        for line in file:
            if 'z' in line:
                z_line += 1
        return z_line

    @staticmethod
    def z_count(file):
        """Counting the number of all occurrences of 'z'."""
        sum_z = 0
        for line in file:
            for letter in line:
                if letter == 'z':
                    sum_z += 1
        return sum_z

    @staticmethod
    def lines_with_and(file):
        """Counting the number of lines containing 'and'."""
        and_string = 0
        for line in file:
            if 'and' in line:
                and_string += 1
        return and_string


def main():
    filename = input('Please, enter a path to file: ')
    with open(filename, 'r') as file:
        print("total lines: ", '{:>6}'.format(FileStatistic.total_lines(file)))
        file.seek(0)
        print("empty lines: ", '{:>6}'.format(FileStatistic.number_of_empty_lines(file)))
        file.seek(0)
        print("lines with 'z':", '{:>4}'.format(FileStatistic.lines_with_z(file)))
        file.seek(0)
        print("'z' count:", '{:>9}'.format(FileStatistic.z_count(file)))
        file.seek(0)
        print("lines with 'and': ", FileStatistic.lines_with_and(file))
        file.close()


if __name__ == '__main__':
    while True:
        main()
        response = input("If one more file needs to be analyzed? (Yes or No) : ").lower()
        if response != 'yes' and response != 'y':
            break
