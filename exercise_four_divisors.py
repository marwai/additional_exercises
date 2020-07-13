# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
# 13 is a divisor of 26 because 26 / 13 has no remainder.)

class program():
    def __init__(self):
        pass

    def number(self):
        # empty list - really good tool to iterate through
        empty = []

        # int import is important when receiving a number
        num = int(input("Divide a number:\n"))

        # make a list of a range starting at 1 and ends on the input number
        list_range = list(range(1, num + 1))
        for number in list_range:

            # if the input is divisible by the number that is iterating
            # through the list
            if num % number == 0:

                # then add this to the empty list
                empty.append(number)
                print(empty)


p = program()
p.number()

