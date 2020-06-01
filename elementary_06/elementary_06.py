"""This program after the user enters a six-digit number, uses two methods
two find a happy ticket. At the end, the program displays the winning method
and the number of happy tickets for each method of counting."""


def easy_finding_happy_ticket(min, max):
    """Using an easy way - if the sum of the first three digits is equal to the sum
    of the last three, then this ticket is considered happy."""
    easy_happy_tickets = 0
    for ticket in range(min, max + 1):
        ticket_nums = list(map(int, str(ticket)))
        if ticket_nums[0] + ticket_nums[1] + ticket_nums[2] == ticket_nums[3] + ticket_nums[4] + ticket_nums[5]:
            easy_happy_tickets += 1
    return easy_happy_tickets


def difficult_finding_happy_ticket(min, max):
    """Using difficult way -  if the sum of the even numbers of the ticket is equal
    to the sum of the odd numbers of the ticket, then the ticket is considered happy."""
    diff_happy_tickets = 0
    for ticket in range(int(min), int(max) + 1):
        even_ticket_nums = [num for num in map(int, str(ticket)) if num % 2 == 0]
        odd_ticket_nums = [num for num in map(int, str(ticket)) if num % 2 == 1]
        if sum(even_ticket_nums) == sum(odd_ticket_nums):
            diff_happy_tickets += 1
    return diff_happy_tickets


if __name__ == '__main__':
    while True:
        min = input("Enter min ticket: ")
        max = input("Enter max ticket: ")
        try:
            int(min)
            int(max)
        except ValueError:
            print('Please, enter the integers! ')
            min = input("Enter min ticket: ")
            max = input("Enter max ticket: ")

        if len(min) == 6 and len(max) == 6:
            easy_way = (easy_finding_happy_ticket(int(min), int(max)))
            diff_way = (difficult_finding_happy_ticket(int(min), int(max)))
            if diff_way > easy_way:
                print(f'Won the difficult way of counting. Using it we found {diff_way} happy tickets!')
                print(f'Using easy method we found {easy_way} happy tickets.')
            else:
                print(f'Won the easy way of counting. Using it we found {easy_way} happy tickets!')
                print(f'Using difficult method we found {diff_way} happy tickets.')

            response = input('Would you like to run the program again (Yes / No)? ').lower()
            if response != 'yes' and response != 'y':
                break
        else:
            print('Please, enter a six digit number ! ')
