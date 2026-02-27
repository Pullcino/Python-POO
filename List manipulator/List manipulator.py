class List_manipulator():


    def __init__(self, list = []):

        self.list = list

    def add_elements(self):

        number = int(input("Digit the number you want to add: "))

        self.list.append(number)

        print(f"{number} added with success")

    def remove_elements(self):

        try:

            number = int(input("Digit the number you want to remove: "))

            self.list.remove(number)

            print(f"{number} removed with success")

        except ValueError:

            print("The list dont have any item\n")


    def found_max(self):

        print(f"The biggest number in the list is: {max(self.list)}")

    def found_min(self):

        print(f"The smallest number in the list is: {min(self.list)}")

    def found_media(self):

        value = sum(self.list)

        media = value / len(self.list)

        print(f"The media is {media}")

    def show_list(self):

        print(f"Thats the list: {self.list}")


def main():

    call = List_manipulator()

    while True:


        print("Welcome to the list manipulator\n")
        print("1 - Add a number.")
        print("2 - Remove a number.")
        print("3 - Found max value.")
        print("4 - Found min value.")
        print("5 - Found list media.")
        print("6 - Show list.")
        print("7 - Leave program.\n")

        choice = input("Choose one of the options.")

        if choice == '1':

            call.add_elements()

        elif choice == '2':

            call.remove_elements()

        elif choice == '3':

            call.found_max()

        elif choice == '4':

            call.found_min()

        elif choice == '5':

            call.found_media()

        elif choice == '6':

            call.show_list()

        elif choice == '7':

            print("You leave the program.")

            break

        else:

            print("That option dont exist")


main()