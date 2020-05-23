def get_count_specific_line(path, string):
    with open(path, 'r') as f:
        count = 0
        for line in f:
            if string in line:
                count += 1.
        print("Total number of lines is:", int(count))


def replace_specific_line(path, string, new_string):
    s = open(path).read()
    s = s.replace(string, new_string)
    f = open(path, 'w')
    f.write(s)
    f.close()


def main():
    while True:
        print("""
File parser counts amount of occurrences of specific line in this way:
< path/to/file.txt >, < string for counting >
If you need to replace the specific line to other -
Please, write the command in this way:
< path/to/file.txt >, < string for searching >, < replacement string >
        """)
        user_input = input("Please, write down 2 or 3 parameters as described above using comma: ").split(', ')
        if len(user_input) == 2:
            path = user_input[0]
            string = user_input[1]
            get_count_specific_line(path, string)
        elif len(user_input) == 3:
            path = user_input[0]
            string = user_input[1]
            new_string = user_input[2]
            replace_specific_line(path, string, new_string)
        else:
            print('Please, enter the correct input! ')

        if input('Would you like to run the program again (Yes / No)? ').lower() != 'yes':
            break


if __name__ == '__main__':
    main()
