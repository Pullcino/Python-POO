"""
Exercício Manipulador de Listas em Python

Objetivo:

Neste exercício, você criará uma aplicação Python que ajuda os usuários a 
manipular listas de números inteiros. A aplicação deve oferecer opções para 
adicionar elementos, remover elementos, encontrar o maior e o menor elemento, 
calcular a média dos elementos e mais.

Requisitos:

    1. Crie uma classe chamada ManipuladorDeLista que será responsável por todas as 
    operações de manipulação de lista.
    
        - adicionar_elemento(elemento): adiciona um elemento no final da lista.
        - remover_elemento(elemento): remove a primeira ocorrência do elemento na lista.
        - encontrar_maior(): encontra e retorna o maior elemento da lista.
        - encontrar_menor(): encontra e retorna o menor elemento da lista.
        - calcular_media(): calcula e retorna a média dos elementos na lista.
        - mostrar_lista(): retorna a lista atual.

    2. Implemente uma função menu() que serve como interface do usuário. Essa 
    função deve mostrar um menu com as opções de manipulação e realizar a operação 
    escolhida pelo usuário.

    3. O programa deve continuar rodando e mostrando o menu até que o usuário escolha sair.

"""


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

            call.