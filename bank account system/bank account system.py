'''Sistema de Conta Bancária

Classe Conta

Métodos: depositar, sacar, transferir

Conceitos: encapsulamento'''

class Bank:

    def __init__(self, balance = 0):

        self.balance = balance

    def deposit(self):

        value = int(input("How much you want to to deposit: \n"))

        self.balance += value

        print(f"Now that is your balance: {self.balance}\n")

    def withdraw(self):

        value = int(input("How much you want to withdraw: \n"))

        self.balance -= value

        print(f"Now that is your balance: {self.balance}\n")

    def show_balance(self):

        print(f"Thats your balance: {self.balance}\n")




def main():

    call = Bank()

    while True:

        print("Welcome to your bank account\n")
        print("1 - Deposit")
        print("2 - Wihtdraw")
        print("3 - Show balance")
        print("4 - Leave\n")

        choice = input("Digit your choice: \n")

        if choice == '1':

            call.deposit()

        elif choice =='2':

            call.withdraw()

        elif choice == '3':

            call.show_balance()

        elif choice == '4':

            print("You leave the system")

            break

        else:

            print("That option don't exist\n")

main()