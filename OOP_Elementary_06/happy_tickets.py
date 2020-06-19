"""
There are 2 ways to count happy tickets:
1. Simple - if a six-digit number is printed on the ticket, and the sum of the first three digits is equal
to the sum of the last three, then this ticket is considered happy.
2. Complex - if the sum of the even numbers of the ticket is equal to the sum of the odd numbers of the
ticket, then the ticket is considered happy.

The program determines which option for counting happy tickets will display a larger number at a given interval.
"""


class FindHappyTicket:
    easy_happy_tickets = 0
    diff_happy_tickets = 0

    @classmethod
    def easy_finding_happy_ticket(cls, min_ticket, max_ticket):
        """
        Using an easy way - if the sum of the first three digits is equal to the sum
        of the last three, then this ticket is considered happy.
        """

        for ticket in range(min_ticket, max_ticket + 1):
            ticket_nums = list(map(int, str(ticket)))
            if ticket_nums[0] + ticket_nums[1] + ticket_nums[2] == ticket_nums[3] + ticket_nums[4] + ticket_nums[5]:
                cls.easy_happy_tickets += 1
        return cls.easy_happy_tickets

    @classmethod
    def difficult_finding_happy_ticket(cls, min_ticket, max_ticket):
        """
        Using difficult way -  if the sum of the even numbers of the ticket is equal
        to the sum of the odd numbers of the ticket, then the ticket is considered happy.
        """

        for ticket in range(int(min_ticket), int(max_ticket) + 1):
            even_ticket_nums = [num for num in map(int, str(ticket)) if num % 2 == 0]
            odd_ticket_nums = [num for num in map(int, str(ticket)) if num % 2 == 1]
            if sum(even_ticket_nums) == sum(odd_ticket_nums):
                cls.diff_happy_tickets += 1
        return cls.diff_happy_tickets


if __name__ == '__main__':
    while True:
        min_ticket = input("Enter min ticket: ")
        max_ticket = input("Enter max ticket: ")
        try:
            int(min_ticket)
            int(max_ticket)
        except ValueError:
            print("Please, enter the integers!")
            min_ticket = input("Enter min ticket: ")
            max_ticket = input("Enter max ticket: ")

        if len(min_ticket) == 6 and len(max_ticket) == 6:
            happy_ticket = FindHappyTicket()
            easy_way = happy_ticket.easy_finding_happy_ticket(int(min_ticket), int(max_ticket))
            diff_way = happy_ticket.difficult_finding_happy_ticket(int(min_ticket), int(max_ticket))

            if diff_way > easy_way:
                print(f"Won the difficult way of counting. Using it we found {diff_way} happy tickets!")
                print(f"Using easy method we found {easy_way} happy tickets.")
            else:
                print(f"Won the easy way of counting. Using it we found {easy_way} happy tickets!")
                print(f"Using difficult method we found {diff_way} happy tickets.")

            response = input("Would you like to run the program again (Yes / No)? ").lower()
            if response != "yes" and response != "y":
                break

        else:
            print("Please, enter a six digit number!")
