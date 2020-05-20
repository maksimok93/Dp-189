filename = input(' Please, enter a path to file: ')
f = open(filename)

while True:
    def main():
        print("total lines: ", '{:>6}'.format(total_lines_()))
        print("empty lines: ", '{:>6}'.format(number_of_empty_lines_()))
        print("lines with 'z':", '{:>4}'.format(lines_with_z_()))
        print("'z' count:", '{:>9}'.format(z_count_()))
        print("lines with 'and': ", lines_with_and_())


    def total_lines_():
        """ Counting the number of all lines in a file """
        f = open(filename)
        total_line = 0
        for line in f:
            total_line += 1
        return total_line


    def number_of_empty_lines_():
        """ counting empty lines """
        f = open(filename)
        empty_line = 0
        for line in f:
            if len(line) == 1:
                empty_line += 1
        return empty_line


    def lines_with_z_():
        """ Output the number of lines with 'z' """
        f = open(filename)
        z_line = 0
        for line in f:
            if 'z' in line:
                z_line += 1
        return z_line


    def z_count_():
        """ counting the number of all occurrences of 'z' """
        f = open(filename)
        sum_z = 0
        for line in f:
            for letter in line:
                if letter == 'z':
                    sum_z += 1
        return sum_z


    def lines_with_and_():
        """ counting the number of lines containing 'and' """
        f = open(filename)
        and_string = 0
        for line in f:
            if 'and' in line:
                and_string += 1
        return and_string


    if __name__ == '__main__':
        main()

        response = input(" If one more file needs to be analyzed? (Yes or No) : ")
        if response == 'Yes':
            filename = input(' Please, enter a path to a file: ')
            f = open(filename)
        else:
            break