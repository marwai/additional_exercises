# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.

class info:
    def __init__(self):
        pass
    def age(self):
        self.age = input("What is your age?")
        self.name = input("What is your name?")
        self.time = 100 - int(self.age)
        self.message = f"Hi {self.name} in {self.time} years you will be 100 years old "
        print(self.message)
        return self.message

info().age()
