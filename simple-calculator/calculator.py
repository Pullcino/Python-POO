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

        self.number1 = int(input("Digit the first number of the division: "))
        self.number2 = int(input("Digit the second number of the division: "))

        result = self.number1 / self.number2

        print(f"The result is: {result}")

    def mult(self):

        self.number1 = int(input("Digit the first number of the multiplication: "))
        self.number2 = int(input("Digit the second number of the multiplication: "))

        result = self.number1 * self.number2

        print(f"The result is: {result}")

def main():


    call = Calculator(0, 0)

    while True:

        print("Welcome to the simple calculator\n")
        print("1 - Sum")
        print("2 - Subtraction")
        print("3 - Division")
        print("4 - Multplication")
        print("5 - Leave\n")

        choice = input("Digit your choice: ")

        if choice == '1':

            call.sum()

        elif choice == '2':

            call.sub()

        elif choice =='3':

            call.div()

        elif choice == '4':

            call.mult()

        elif choice == '5':

            print("You leave the program.")

            break

        else:
            print("That option dont exist.")

main()
        

