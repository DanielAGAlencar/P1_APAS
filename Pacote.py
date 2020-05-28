import jsons
import pymongo
from Regex import Regex
from ValidaRelacoes import ValidaRelacoes
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbtraportadora"]
mycolPacote = mydb["pacote"]

class Relacao_Pacote_Operador_Agencia_Cliente:
    def __init__(self, cpf_cliente, nome_cliente, cnpj_agencia, nome_agencia, n_matricula_op, nome_op):
        self.cpf_cliente = cpf_cliente
        self.nome_cliente = nome_cliente
        self.cnpj_agencia = cnpj_agencia
        self.nome_agencia = nome_agencia
        self.n_matricula_op = n_matricula_op
        self.nome_op = nome_op

class Pacote:


    def __init__(self, nome_dest, cpf_dest, peso, cubagem, logradouro, numero, bairro, cep, cidade, uf, complemento, relacoes):
        self.nome_dest = nome_dest
        self.cpf_dest = cpf_dest
        self.peso =peso
        self.cubagem = cubagem
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
        self.complemento = complemento
        self.relacoes = relacoes

    def inserir_pacote(pacote):
        result = mycolPacote.insert_one(jsons.dump(pacote))
        if result.inserted_id:
            print(f'\nO cadastro do pacote foi inserido com sucesso.')

    def preencher_pacote():
        nome_dest = (input('\nInforme o nome do destinatario: '))
        d = True
        while(d):
            cpf_dest = (input('\nInforme o CPF do destinatario: '))
            d = Regex.valida_cpf(cpf_dest)
        peso = (input('\nInforme o peso: '))
        cubagem = (input('\nInforme a cubagem: '))
        logradouro = (input('\nInforme o logradouro do destinatario: '))
        numero = (input('\nInforme o numero do destinatario: '))
        bairro = (input('\nInforme o bairro do destinatario: '))
        cep = (input('\nInforme o cep do destinatario: '))
        cidade = (input('\nInforme a cidade do destinatario: '))
        uf = (input('\nInforme o estado do destinatario: '))
        complemento = (input('\nInforme o complemento do destinatario: '))
        a = True
        while (a):
            cpf_cliente = (input('\nInforme o CPF do Cliente/Remetente: '))
            a = ValidaRelacoes.valida_cpf_cliente(cpf_cliente)
        nome_cliente = ValidaRelacoes.preenche_nome_cliente(cpf_cliente)
        b = True
        while (b):
            cnpj_agencia = (input('\nInforme o CNPJ da Agência: '))
            b = ValidaRelacoes.valida_cnpj_agencia(cnpj_agencia)
        nome_agencia = ValidaRelacoes.preenche_nome_agencia(cnpj_agencia)
        c = True
        while (c):
            n_matricula_op = (input('\nInforme o numero de matricula do operador: '))
            c = ValidaRelacoes.valida_n_matricula_operador(n_matricula_op)
        nome_op = ValidaRelacoes.preenche_nome_operador(n_matricula_op)
        relacoes = Relacao_Pacote_Operador_Agencia_Cliente(cpf_cliente, nome_cliente, cnpj_agencia, nome_agencia, n_matricula_op, nome_op)
        pacote = Pacote(nome_dest, cpf_dest, peso, cubagem, logradouro, numero, bairro, cep, cidade, uf, complemento, relacoes)
        return pacote

    def atualizar_pacote(id, pacote):
        result = mycolPacote.update_one({'_id': ObjectId(id)}, {"$set": pacote.__dict__})
        if result.modified_count > 0:
            print(f'\nO pacote foi alterado com sucesso.')

    def excluir_pacote(id):
        mycolPacote.delete_one({"_id": ObjectId(id)})
        print("Pacote excluído com sucesso!")

    def cons_pacote_cpf_cliente(cpf):
        myquery = {"relacoes.cpf_cliente": {"$regex": cpf}}
        mydoc = mycolPacote.find(myquery)
        for x in mydoc:
            print(x)

    def cons_id_pacote(id):
        myquery = {"_id": ObjectId(id)}
        mydoc = mycolPacote.find(myquery)
        for x in mydoc:
            print(x)

    def listar_pacote():
        mydoc = mycolPacote.find().sort("_id", 1)
        for x in mydoc:
            print(x)


class Pacote_Menu:
    def pacote_menu():

        def pacote():

            def pacote_opcao():
                print('=================================')
                print("--> 1 - Voltar ao Menu Principal")
                print("--> 2 - Voltar ao Menu de Pacote")
                print("--> 3 - Encerrar Programa")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    from Menu import Menu
                    Menu.menu()
                if opcao == 2:
                    pacote()
                if opcao == 3:
                    exit()
                if opcao != 1 and opcao != 2:
                    print("=====Digite uma opção valida=====")
                    pacote_opcao()

            def consulta_pacote():
                print('=================================')
                print("--> 1 - Consulta por CPF do Cliente")
                print("--> 2 - Consulta por ID")
                print("--> 3 - Listar Todos os Pacotes")
                opcao = int(input("Digite a opção desejada: "))
                print('=================================')
                if opcao == 1:
                    from Pacote import Pacote
                    cpf = str(input("\nInforme o CPF do cliente: "))
                    Pacote.cons_pacote_cpf_cliente(cpf)
                    pacote_opcao()
                if opcao == 2:
                    from Pacote import Pacote
                    id = str(input("\nInforme o ID do Pacote: "))
                    Pacote.cons_id_pacote(id)
                    pacote_opcao()
                if opcao == 3:
                    from Pacote import Pacote
                    Pacote.listar_pacote()
                    pacote_opcao()
                if opcao != 1 and opcao != 2 and opcao != 3:
                    print("=====Digite uma opção valida=====")
                    consulta_pacote()

            print('=================================')
            print("--> 1 - Para Cadastrar Pacote")
            print("--> 2 - Para Alterar  Pacote")
            print("--> 3 - Para Excluir Pacote")
            print("--> 4 - Para Consultar Pacote")
            print("--> 5 - Para Voltar ao Menu Anterior")
            print("--> 6 - Encerrar o Programa")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                from Pacote import Pacote
                Pacote.inserir_pacote(Pacote.preencher_pacote())
                pacote_opcao()
            if opcao == 2:
                from Pacote import Pacote
                id = str(input("\nInforme o id do Pacote: "))
                Pacote.atualizar_pacote(id, Pacote.preencher_pacote())
                pacote_opcao()
            if opcao == 3:
                from Pacote import Pacote
                id = str(input("\nInforme o id do Pacote: "))
                Pacote.excluir_pacote(id)
                pacote_opcao()
            if opcao == 4:
                consulta_pacote()
            if opcao == 5:
                from Menu import Menu
                Menu.menu()
            if opcao == 6:
                exit()
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print("=====Digite uma opção valida=====")
                pacote()

        pacote()

