import jsons
import pymongo
from Regex import Regex
from ValidaRelacoes import ValidaRelacoes


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbtraportadora"]
mycolCliente = mydb["cliente"]

class Cliente:


    def __init__(self, id, nome, cpf, logradouro, numero, bairro, cep, cidade, uf, complemento):
        self.id =id
        self.nome = nome
        self.cpf = cpf
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
        self.complemento = complemento

    def inserir_cliente(cliente):
        result = mycolCliente.insert_one(jsons.dump(cliente))
        if result.inserted_id:
            print(f'\nO cadastro da agência foi inserido com sucesso.')


    def preencher_cliente():
        i = 0
        for x in mycolCliente.find({}, {"_id": 0, "id": 1}):
            y = (str(x).replace("{'id': '", ''))
            z = (y.replace("'}", ''))
            n = (int(z))
            if i < n:
                i = n
            else:
                i = i
        i = i + 1
        print("\nO ID do Cliente será: ", i)
        id = (str(i))
        nome = (input('\nInforme a nome: '))
        b = True
        while(b):
            cpf = (input('\nInforme o CPF: '))
            b = Regex.valida_cpf(cpf)
            c = True
            while(c):
                c = ValidaRelacoes.valida_cpf_cliente_cad(cpf)
                if c == True:
                    b = c
                    c = False
        logradouro = (input('\nInforme o logradouro: '))
        numero = (input('\nInforme o numero: '))
        bairro = (input('\nInforme o bairro: '))
        cep = (input('\nInforme o cep: '))
        cidade = (input('\nInforme a cidade: '))
        uf = (input('\nInforme o estado: '))
        complemento = (input('\nInforme o complemento: '))
        cliente = Cliente(id, nome, cpf, logradouro, numero, bairro, cep, cidade, uf, complemento)
        return cliente

    def atualizar_cliente(id, cliente):
        result = mycolCliente.update_one({'id': id}, {"$set": cliente.__dict__})
        if result.modified_count > 0:
            print(f'\nO cliente foi alterado com sucesso.')

    def excluir_cliente(id):
        mycolCliente.delete_one({"id": id})
        print("Cliente excluído com sucesso!")

    def cons_nome_cliente(nome):
        myquery = {"nome": {"$regex": nome}}
        mydoc = mycolCliente.find(myquery)
        for x in mydoc:
            print(x)

    def cons_id_cliente(id):
        myquery = {"id": id}
        mydoc = mycolCliente.find(myquery)
        for x in mydoc:
            print(x)

    def listar_cliente():
        mydoc = mycolCliente.find().sort("id", 1)
        for x in mydoc:
            print(x)


class Cliente_Menu:
    def cliente_menu():

        def cliente():

            def cliente_opcao():
                print('=================================')
                print("--> 1 - Voltar ao Menu Principal")
                print("--> 2 - Voltar ao Menu de  Cliente")
                print("--> 3 - Encerrar Programa")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    from Menu import Menu
                    Menu.menu()
                if opcao == 2:
                    cliente()
                if opcao == 3:
                    exit()
                if opcao != 1 and opcao != 2:
                    print("=====Digite uma opção valida=====")
                    cliente_opcao()

            def consulta_cliente():
                print('=================================')
                print("--> 1 - Consulta por Nome")
                print("--> 2 - Consulta por ID")
                print("--> 3 - Listar Todos os Clientes")
                opcao = int(input("Digite a opção desejada: "))
                print('=================================')
                if opcao == 1:
                    from Cliente import Cliente
                    nome = str(input("\nInforme o Nome do Cliente: "))
                    Cliente.cons_nome_cliente(nome)
                    cliente_opcao()
                if opcao == 2:
                    from Cliente import Cliente
                    id = str(input("\nInforme o ID da Cliente: "))
                    Cliente.cons_id_cliente(id)
                    cliente_opcao()
                if opcao == 3:
                    from Cliente import Cliente
                    Cliente.listar_cliente()
                    cliente_opcao()
                if opcao != 1 and opcao != 2 and opcao != 3:
                    print("=====Digite uma opção valida=====")
                    consulta_cliente()

            print('=================================')
            print("--> 1 - Para Cadastrar Cliente")
            print("--> 2 - Para Alterar  Cliente")
            print("--> 3 - Para Excluir Cliente")
            print("--> 4 - Para Consultar Cliente")
            print("--> 5 - Para Voltar ao Menu Anterior")
            print("--> 6 - Encerrar o Programa")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                from Cliente import Cliente
                Cliente.inserir_cliente(Cliente.preencher_cliente())
                cliente_opcao()
            if opcao == 2:
                from Cliente import Cliente
                id = str(input("\nInforme o id do Cliente: "))
                Cliente.atualizar_cliente(id, Cliente.preencher_cliente())
                cliente_opcao()
            if opcao == 3:
                from Cliente import Cliente
                id = str(input("\nInforme o id do Cliente: "))
                Cliente.excluir_cliente(id)
                cliente_opcao()
            if opcao == 4:
                consulta_cliente()
            if opcao == 5:
                from Menu import Menu
                Menu.menu()
            if opcao == 6:
                exit()
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print("=====Digite uma opção valida=====")
                cliente()

        cliente()

