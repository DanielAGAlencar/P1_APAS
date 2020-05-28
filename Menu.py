from Agencia import Agencia_Menu
from Operador import Operador_Menu
from Cliente import Cliente_Menu
from Pacote import Pacote_Menu
from CadStatus import CadStatus_Menu
from StatusPacote import StatusPacote_Menu

class Menu:

    def menu():
        print('=================================')
        print("--> 1 - Para Agencia")
        print("--> 2 - Para Operador")
        print("--> 3 - Para Cliente")
        print("--> 4 - Para Pacote")
        print("--> 5 - Para Cadastro de Status")
        print("--> 6 - Para Status de Pacotes")
        print("--> 7 - Encerrar o Programa")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            Agencia_Menu.agencia_menu()
        if opcao == 2:
            Operador_Menu.operador_menu()
        if opcao == 3:
            Cliente_Menu.cliente_menu()
        if opcao == 4:
            Pacote_Menu.pacote_menu()
        if opcao == 5:
            CadStatus_Menu.cadstatus_menu()
        if opcao == 6:
            StatusPacote_Menu.statuspacote_menu()
        if opcao == 7:
            exit()
        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 7:
            print("=====Digite uma opção valida=====")
            Menu.menu()

    menu()