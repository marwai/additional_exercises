# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the
# user. Hint: how does an even / odd number react differently when divided by 2?
import math

class info():
    def __init__(self):
        pass

    def question(self):
        self.question = input("choose a number?")
        if (float(self.question)) % 2 == 0:
            print("This is even")
        else:
            print("This is odd")
        return self.question
a = info()
a.question()