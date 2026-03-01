class Calculator:

    def __init__(self, number1, number2):

        self.number1 = number1
        self.number2 = number2

    def sum(self):

        self.number1 = int(input("Digit the first number of the sum: "))
        self.number2 = int(input("Digit the second number of the sum: "))

        result = self.number1 + self.number2

        print(f"The result is: {result}")
    
    def sub(self):

        self.number1 = int(input("Digit the first number of the subtraction: "))
        self.number2 = int(input("Digit the second number of the subtraction: "))

        result = self.number1 - self.number2

        print(f"The result is: {result}")

    def div(self):

        self.number1 = int(input("Digit the first number of the sum: "))
        self.number2 = int(input("Digit the second number of the sum: "))

        result = self.number1 / self.number2

        print(f"The result is: {result}")

    def mult(self):

        self.number1 = int(input("Digit the first number of the sum: "))
        self.number2 = int(input("Digit the second number of the sum: "))

        result = self.number1 * self.number2

        print(f"The result is: {result}")

def main():


    call = call.Calculator

