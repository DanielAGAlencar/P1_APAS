import jsons
import pymongo
from Regex import Regex
from ValidaRelacoes import ValidaRelacoes
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbtraportadora"]
mycolStatusPacote = mydb["statuspacote"]

class Relacao_StautsPacote_Operador_Agencia:
    def __init__(self, cod_pacote, cnpj_agencia, nome_agencia, n_matricula_op, nome_op):
        self.cod_pacote = cod_pacote
        self.cnpj_agencia = cnpj_agencia
        self.nome_agencia = nome_agencia
        self.n_matricula_op = n_matricula_op
        self.nome_op = nome_op

class StatusPacote:


    def __init__(self, status, cpf_cliente, nome_cliente, relacoes):
        self.status = status
        self.cpf_cliente = cpf_cliente
        self.nome_cliente = nome_cliente
        self.relacoes = relacoes

    def inserir_statuspacote(statuspacote):
        result = mycolStatusPacote.insert_one(jsons.dump(statuspacote))
        if result.inserted_id:
            print(f'\nO status do pacote foi inserido com sucesso.')

    def preencher_statuspacote():
        a = True
        while(a):
            id = (input('\nInforme o id status: '))
            a = ValidaRelacoes.valida_id_status(id)
        status = ValidaRelacoes.preenche_desc_status(id)
        d = True
        while(d):
            cpf_cliente = (input("\nInforme o CPF do cliente: "))
            d = ValidaRelacoes.valida_cpf_cliente(cpf_cliente)
        nome_cliente = ValidaRelacoes.preenche_nome_cliente(cpf_cliente)
        cod_pacote = (input('\nInforme a codigo do pacote: '))
        b = True
        while(b):
            cnpj_agencia = (input('\nInforme o CNPJ da agência: '))
            b = ValidaRelacoes.valida_cnpj_agencia(cnpj_agencia)
        nome_agencia = ValidaRelacoes.preenche_nome_agencia(cnpj_agencia)
        c = True
        while(c):
            n_matricula_op = (input('\nInforme o numero de matricula do operador: '))
            c = ValidaRelacoes.valida_n_matricula_operador(n_matricula_op)
        nome_op = ValidaRelacoes.preenche_nome_operador(n_matricula_op)
        relacoes = Relacao_StautsPacote_Operador_Agencia(cod_pacote, cnpj_agencia, nome_agencia, n_matricula_op, nome_op)
        statuspacote = StatusPacote(status, cpf_cliente, nome_cliente, relacoes)
        return statuspacote

    def atualizar_statuspacote(id, statuspacote):
        result = mycolStatusPacote.update_one({'_id': ObjectId(id)}, {"$set": statuspacote.__dict__})
        if result.modified_count > 0:
            print(f'\nO status do pacote foi alterado com sucesso.')

    def excluir_statuspacote(id):
        mycolStatusPacote.delete_one({'_id': ObjectId(id)})
        print("Status do pacote excluído com sucesso!")

    def cons_statuspacote_cpf_cliente(cpf):
        myquery = {"cpf_cliente": cpf}
        mydoc = mycolStatusPacote.find(myquery)
        for x in mydoc:
            print(x)

    def cons_cod_pacote(cod):
        myquery = {"relacoes.cod_pacote": cod}
        mydoc = mycolStatusPacote.find(myquery)
        for x in mydoc:
            print(x)

    def listar_statuspacote():
        mydoc = mycolStatusPacote.find().sort("_id", 1)
        for x in mydoc:
            print(x)


class StatusPacote_Menu:
    def statuspacote_menu():

        def statuspacote():

            def statuspacote_opcao():
                print('=================================')
                print("--> 1 - Voltar ao Menu Principal")
                print("--> 2 - Voltar ao Menu de Status de Pacote")
                print("--> 3 - Encerrar Programa")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    from Menu import Menu
                    Menu.menu()
                if opcao == 2:
                    statuspacote()
                if opcao == 3:
                    exit()
                if opcao != 1 and opcao != 2:
                    print("=====Digite uma opção valida=====")
                    statuspacote_opcao()

            def consulta_statuspacote():
                print('=================================')
                print("--> 1 - Consulta por CPF do cliente")
                print("--> 2 - Consulta por Código do Pacote")
                print("--> 3 - Listar Todos os Pacotes")
                opcao = int(input("Digite a opção desejada: "))
                print('=================================')
                if opcao == 1:
                    from StatusPacote import StatusPacote
                    cpf = str(input("\nInforme o CPF do cliente: "))
                    StatusPacote.cons_statuspacote_cpf_cliente(cpf)
                    statuspacote_opcao()
                if opcao == 2:
                    from StatusPacote import StatusPacote
                    id = str(input("\nInforme o ID do Pacote: "))
                    StatusPacote.cons_cod_pacote(id)
                    statuspacote_opcao()
                if opcao == 3:
                    from StatusPacote import StatusPacote
                    StatusPacote.listar_statuspacote()
                    statuspacote_opcao()
                if opcao != 1 and opcao != 2 and opcao != 3:
                    print("=====Digite uma opção valida=====")
                    consulta_statuspacote()

            print('=================================')
            print("--> 1 - Para Cadastrar Status de Pacote")
            print("--> 2 - Para Alterar Status de Pacote")
            print("--> 3 - Para Excluir Status de Pacote")
            print("--> 4 - Para Consultar Status de Pacote")
            print("--> 5 - Para Voltar ao Menu Anterior")
            print("--> 6 - Encerrar o Programa")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                from StatusPacote import StatusPacote
                StatusPacote.inserir_statuspacote(StatusPacote.preencher_statuspacote())
                statuspacote_opcao()
            if opcao == 2:
                from StatusPacote import StatusPacote
                id = str(input("\nInforme o id do Pacote: "))
                StatusPacote.atualizar_statuspacote(id, StatusPacote.preencher_statuspacote())
                statuspacote_opcao()
            if opcao == 3:
                from StatusPacote import StatusPacote
                id = str(input("\nInforme o id do Pacote: "))
                StatusPacote.excluir_statuspacote(id)
                statuspacote_opcao()
            if opcao == 4:
                consulta_statuspacote()
            if opcao == 5:
                from Menu import Menu
                Menu.menu()
            if opcao == 6:
                exit()
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print("=====Digite uma opção valida=====")
                statuspacote()

        statuspacote()

