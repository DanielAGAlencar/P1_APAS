import jsons
import pymongo
from Regex import Regex
from ValidaRelacoes import ValidaRelacoes


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbtraportadora"]
mycolAgencia = mydb["agencia"]

class Agencia:

    def __init__(self, id, nome, cnpj, logradouro, numero, bairro, cep, cidade, uf, complemento):
        self.id =id
        self.nome = nome
        self.cnpj = cnpj
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
        self.complemento = complemento

    def inserir_agencia(agencia):
        result = mycolAgencia.insert_one(jsons.dump(agencia))
        if result.inserted_id:
            print(f'\nO cadastro da agência foi inserido com sucesso.')


    def preencher_agencia():
        i = 0
        for x in mycolAgencia.find({}, {"_id": 0, "id": 1}):
            y = (str(x).replace("{'id': '", ''))
            z = (y.replace("'}", ''))
            n = (int(z))
            if i < n:
                i = n
            else:
                i = i
        i = i + 1
        print("\nO ID do Agência será: ", i)
        id = (str(i))
        nome = (input('\nInforme a nome: '))
        b = True
        while(b):
            cnpj = (input('\nInforme o CNPJ: '))
            b = Regex.valida_cnpj(cnpj)
            c = True
            while(c):
                c = ValidaRelacoes.valida_cnpj_agencia_cad(cnpj)
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
        agencia = Agencia(id, nome, cnpj, logradouro, numero, bairro, cep, cidade, uf, complemento)
        return agencia

    def atualizar_agencia(id, agencia):
        result = mycolAgencia.update_one({'id': id}, {"$set": agencia.__dict__})
        if result.modified_count > 0:
            print(f'\nA agência foi alterado com sucesso.')

    def excluir_agencia(id):
        mycolAgencia.delete_one({"id": id})
        print("Agência excluído com sucesso!")

    def cons_nome_agencia(nome):
        myquery = {"nome": {"$regex": nome}}
        mydoc = mycolAgencia.find(myquery)
        for x in mydoc:
            print(x)

    def cons_id_agencia(id):
        myquery = {"id": id}
        mydoc = mycolAgencia.find(myquery)
        for x in mydoc:
            print(x)

    def listar_agencia():
        mydoc = mycolAgencia.find().sort("id", 1)
        for x in mydoc:
            print(x)


class Agencia_Menu:
    def agencia_menu():

        def agencia():

            def agencia_opcao():
                print('=================================')
                print("--> 1 - Voltar ao Menu Principal")
                print("--> 2 - Voltar ao Menu de  Agência")
                print("--> 3 - Encerrar Programa")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    from Menu import Menu
                    Menu.menu()
                if opcao == 2:
                    agencia()
                if opcao == 3:
                    exit()
                if opcao != 1 and opcao != 2:
                    print("=====Digite uma opção valida=====")
                    agencia_opcao()

            def consulta_agencia():
                print('=================================')
                print("--> 1 - Consulta por Nome")
                print("--> 2 - Consulta por ID")
                print("--> 3 - Listar Todos as Agências")
                opcao = int(input("Digite a opção desejada: "))
                print('=================================')
                if opcao == 1:
                    from Agencia import Agencia
                    nome = str(input("\nInforme o Nome do Cliente: "))
                    Agencia.cons_nome_agencia(nome)
                    agencia_opcao()
                if opcao == 2:
                    from Agencia import Agencia
                    id = str(input("\nInforme o ID da Agência: "))
                    Agencia.cons_id_agencia(id)
                    agencia_opcao()
                if opcao == 3:
                    from Agencia import Agencia
                    Agencia.listar_agencia()
                    agencia_opcao()
                if opcao != 1 and opcao != 2 and opcao != 3:
                    print("=====Digite uma opção valida=====")
                    consulta_agencia()

            print('=================================')
            print("--> 1 - Para Cadastrar Agência")
            print("--> 2 - Para Alterar  Agência")
            print("--> 3 - Para Excluir Agência")
            print("--> 4 - Para Consultar Agência")
            print("--> 5 - Para Voltar ao Menu Anterior")
            print("--> 6 - Encerrar o Programa")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                from Agencia import Agencia
                Agencia.inserir_agencia(Agencia.preencher_agencia())
                agencia_opcao()
            if opcao == 2:
                from Agencia import Agencia
                id = str(input("\nInforme o id do Agência: "))
                Agencia.atualizar_agencia(id, Agencia.preencher_agencia())
                agencia_opcao()
            if opcao == 3:
                from Agencia import Agencia
                id = str(input("\nInforme o id do Agência: "))
                Agencia.excluir_agencia(id)
                agencia_opcao()
            if opcao == 4:
                consulta_agencia()
            if opcao == 5:
                from Menu import Menu
                Menu.menu()
            if opcao == 6:
                exit()
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print("=====Digite uma opção valida=====")
                agencia()

        agencia()

