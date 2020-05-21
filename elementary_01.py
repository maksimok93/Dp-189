a = int(input("Enter the width of the picture: "))
symbol = '*'
space = ' '

for i in range(1, a + 1):
    if (i + 2) % 2 == 0:
        print(a * (space + symbol))
    else:
        print(a * (symbol + space))
