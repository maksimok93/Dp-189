class Envelope:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @staticmethod
    def output_ok():
        print("The 2nd envelope can be placed in the 1st.")

    @staticmethod
    def output_wrong():
        print("The 2nd envelope can't be placed in the 1st")

    def check_envelope_sides(self):
        if self.d > self.c:
            if (self.c <= self.a and self.c <= self.b) and (self.d <= self.a or self.d <= self.b):
                return self.output_ok()
            else:
                return self.output_wrong()

        elif self.c > self.d:
            if (self.d <= self.a and self.d <= self.b) and (self.c <= self.a or self.c <= self.b):
                return self.output_ok()
            else:
                return self.output_wrong()
        else:
            if (self.d <= self.a and self.d <= self.b) and (self.c <= self.a and self.c <= self.b):
                return self.output_ok()
            else:
                return self.output_wrong()


if __name__ == '__main__':
    while True:
        try:
            a = float(input("Enter the 1st side of 1st envelope: "))
            b = float(input("Enter the 2nd side of 1st envelope: "))
            c = float(input("Enter the 1st side of 2nd envelope: "))
            d = float(input("Enter the 2nd side of 2nd envelope: "))

            if a <= 0:
                raise ValueError
            elif b <= 0:
                raise ValueError
            elif c <= 0:
                raise ValueError
            elif d <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please, enter a positive numbers! ")

    envelopes = Envelope(a, b, c, d)
    envelopes.check_envelope_sides()
