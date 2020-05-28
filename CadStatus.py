import jsons
import pymongo
from Regex import Regex


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbtraportadora"]
mycolCadStatus = mydb["cadstatus"]

class CadStatus:


    def __init__(self, id, descricao):
        self.id =id
        self.descricao = descricao


    def inserir_cadstatus(cadstatus):
        result = mycolCadStatus.insert_one(jsons.dump(cadstatus))
        if result.inserted_id:
            print(f'\nO cadastro do status foi inserido com sucesso.')


    def preencher_cadstatus():
        i = 0
        for x in mycolCadStatus.find({}, {"_id": 0, "id": 1}):
            y = (str(x).replace("{'id': '", ''))
            z = (y.replace("'}", ''))
            n = (int(z))
            if i < n:
                i = n
            else:
                i = i
        i = i + 1
        print("\nO ID do Status será: ", i)
        id = (str(i))
        descricao = (input('\nInforme a descrição: '))
        cadstatus = CadStatus(id, descricao)
        return cadstatus

    def atualizar_cadstatus(id, cadstatus):
        result = mycolCadStatus.update_one({'id': id}, {"$set": cadstatus.__dict__})
        if result.modified_count > 0:
            print(f'\nO cadastro do status foi alterado com sucesso.')

    def excluir_cadstatus(id):
        mycolCadStatus.delete_one({"id": id})
        print("O cadastro do status excluído com sucesso!")

    def cons_nome_cadstatus(descricao):
        myquery = {"descricao": {"$regex": descricao}}
        mydoc = mycolCadStatus.find(myquery)
        for x in mydoc:
            print(x)

    def cons_id_cadstatus(id):
        myquery = {"id": id}
        mydoc = mycolCadStatus.find(myquery)
        for x in mydoc:
            print(x)

    def listar_cadstatus():
        mydoc = mycolCadStatus.find().sort("id", 1)
        for x in mydoc:
            print(x)


class CadStatus_Menu:
    def cadstatus_menu():

        def cadstatus():

            def cadstatus_opcao():
                print('=================================')
                print("--> 1 - Voltar ao Menu Principal")
                print("--> 2 - Voltar ao Menu de Cadastro de Status")
                print("--> 3 - Encerrar Programa")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    from Menu import Menu
                    Menu.menu()
                if opcao == 2:
                    cadstatus()
                if opcao == 3:
                    exit()
                if opcao != 1 and opcao != 2:
                    print("=====Digite uma opção valida=====")
                    cadstatus_opcao()

            def consulta_cadstatus():
                print('=================================')
                print("--> 1 - Consulta por Descrição")
                print("--> 2 - Consulta por ID")
                print("--> 3 - Listar Todos os Cadastros de Status")
                opcao = int(input("Digite a opção desejada: "))
                print('=================================')
                if opcao == 1:
                    from CadStatus import CadStatus
                    descricao = str(input("\nInforme a Descrição do Status: "))
                    CadStatus.cons_nome_cadstatus(descricao)
                    cadstatus_opcao()
                if opcao == 2:
                    from CadStatus import CadStatus
                    id = str(input("\nInforme o ID da Cliente: "))
                    CadStatus.cons_id_cadstatus(id)
                    cadstatus_opcao()
                if opcao == 3:
                    from CadStatus import CadStatus
                    CadStatus.listar_cadstatus()
                    cadstatus_opcao()
                if opcao != 1 and opcao != 2 and opcao != 3:
                    print("=====Digite uma opção valida=====")
                    consulta_cadstatus()

            print('=================================')
            print("--> 1 - Para Cadastrar Status")
            print("--> 2 - Para Alterar  Status")
            print("--> 3 - Para Excluir Status")
            print("--> 4 - Para Consultar Status")
            print("--> 5 - Para Voltar ao Menu Anterior")
            print("--> 6 - Encerrar o Programa")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                from CadStatus import CadStatus
                CadStatus.inserir_cadstatus(CadStatus.preencher_cadstatus())
                cadstatus_opcao()
            if opcao == 2:
                from CadStatus import CadStatus
                id = str(input("\nInforme o id do Cliente: "))
                CadStatus.atualizar_cadstatus(id, CadStatus.preencher_cadstatus())
                cadstatus_opcao()
            if opcao == 3:
                from CadStatus import CadStatus
                id = str(input("\nInforme o id do Cliente: "))
                CadStatus.excluir_cadstatus(id)
                cadstatus_opcao()
            if opcao == 4:
                consulta_cadstatus()
            if opcao == 5:
                from Menu import Menu
                Menu.menu()
            if opcao == 6:
                exit()
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print("=====Digite uma opção valida=====")
                cadstatus()

        cadstatus()