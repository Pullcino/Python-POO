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
        