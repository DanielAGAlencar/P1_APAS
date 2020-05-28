import jsons
import pymongo
from Regex import Regex
from ValidaRelacoes import ValidaRelacoes


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbtraportadora"]
mycolOperador = mydb["operador"]

class Relacao_Operador_Agencia:
    def __init__(self, cnpj_agencia, nome_agencia):
        self.cnpj_agencia = cnpj_agencia
        self.nome_agencia = nome_agencia

class Operador:


    def __init__(self, id, nome, cpf, n_matricula, turno, relacao_agencia):
        self.id =id
        self.nome = nome
        self.cpf = cpf
        self.n_matricula = n_matricula
        self.turno = turno
        self.relacao_agencia = relacao_agencia

    def inserir_operador(operador):
        result = mycolOperador.insert_one(jsons.dump(operador))
        if result.inserted_id:
            print(f'\nO cadastro do operador foi inserido com sucesso.')

    def preencherid_operador():
        i = 1
        for x in mycolOperador.find({}, {"_id": 0, "id": 1}):
            y = (str(x).replace("{'id': '", ''))
            z = (y.replace("'}", ''))
            n = (int(z))
            if i < n:
                i = n
            else:
                i = i
        i = i + 1
        print("\nO ID do Operador será: ", i)
        return i

    def preencher_operador():
        i = 0
        for x in mycolOperador.find({}, {"_id": 0, "id": 1}):
            y = (str(x).replace("{'id': '", ''))
            z = (y.replace("'}", ''))
            n = (int(z))
            if i < n:
                i = n
            else:
                i = i
        i = i + 1
        print("\nO ID do Operador será: ", i)
        id = (str(i))
        #(input('\nInforme o id: '))
        nome = (input('\nInforme a nome: '))
        c = True
        while(c):
            cpf = (input('\nInforme o CPF: '))
            c = Regex.valida_cpf(cpf)
            b = True
            while(b):
                b = ValidaRelacoes.valida_cpf_operador_cad(cpf)
                if b == True:
                    c = b
                    b = False
        d = True
        while(d):
            n_matricula = (input('\nInforme o Numero de Matrícula: '))
            d = Regex.valida_n_matricula(n_matricula)
            e = True
            while(e):
                e = ValidaRelacoes.valida_n_matricula_operador_cad(n_matricula)
                if e == True:
                    d = e
                    e = False
        turno = (input('\nInforme o turno: '))
        b = True
        while (b):
            cnpj_agencia = (input('\nInforme o CNPJ da Agência: '))
            b = ValidaRelacoes.valida_cnpj_agencia(cnpj_agencia)
        nome_agencia = ValidaRelacoes.preenche_nome_agencia(cnpj_agencia)
        relacao_agencia = Relacao_Operador_Agencia(cnpj_agencia, nome_agencia)
        operador = Operador(id, nome, cpf, n_matricula, turno, relacao_agencia)
        return operador

    def atualizar_operador(id, operador):
        result = mycolOperador.update_one({'id': id}, {"$set": operador.__dict__})
        if result.modified_count > 0:
            print(f'\nO operador foi alterado com sucesso.')

    def excluir_operador(id):
        mycolOperador.delete_one({"id": id})
        print("Operador excluído com sucesso!")

    def cons_nome_operador(nome):
        myquery = {"nome": {"$regex": nome}}
        mydoc = mycolOperador.find(myquery)
        for x in mydoc:
            print(x)

    def cons_id_operador(id):
        myquery = {"id": id}
        mydoc = mycolOperador.find(myquery)
        for x in mydoc:
            print(x)

    def listar_operador():
        mydoc = mycolOperador.find().sort("id", 1)
        for x in mydoc:
            print(x)


class Operador_Menu:
    def operador_menu():

        def operador():

            def operador_opcao():
                print('=================================')
                print("--> 1 - Voltar ao Menu Principal")
                print("--> 2 - Voltar ao Menu de Operador")
                print("--> 3 - Encerrar Programa")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    from Menu import Menu
                    Menu.menu()
                if opcao == 2:
                    operador()
                if opcao == 3:
                    exit()
                if opcao != 1 and opcao != 2:
                    print("=====Digite uma opção valida=====")
                    operador_opcao()

            def consulta_operador():
                print('=================================')
                print("--> 1 - Consulta por Nome")
                print("--> 2 - Consulta por ID")
                print("--> 3 - Listar Todos as Operadores")
                opcao = int(input("Digite a opção desejada: "))
                print('=================================')
                if opcao == 1:
                    from Operador import Operador
                    nome = str(input("\nInforme o Nome do Operador: "))
                    Operador.cons_nome_operador(nome)
                    operador_opcao()
                if opcao == 2:
                    from Operador import Operador
                    id = str(input("\nInforme o ID do Operador: "))
                    Operador.cons_id_operador(id)
                    operador_opcao()
                if opcao == 3:
                    from Operador import Operador
                    Operador.listar_operador()
                    operador_opcao()
                if opcao != 1 and opcao != 2 and opcao != 3:
                    print("=====Digite uma opção valida=====")
                    consulta_operador()

            print('=================================')
            print("--> 1 - Para Cadastrar Operador")
            print("--> 2 - Para Alterar  Operador")
            print("--> 3 - Para Excluir Operador")
            print("--> 4 - Para Consultar Operador")
            print("--> 5 - Para Voltar ao Menu Anterior")
            print("--> 6 - Encerrar o Programa")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                from Operador import Operador
                Operador.inserir_operador(Operador.preencher_operador())
                operador_opcao()
            if opcao == 2:
                from Operador import Operador
                id = str(input("\nInforme o id do Operador: "))
                Operador.atualizar_operador(id, Operador.preencher_operador())
                operador_opcao()
            if opcao == 3:
                from Operador import Operador
                id = str(input("\nInforme o id do Operador: "))
                Operador.excluir_operador(id)
                operador_opcao()
            if opcao == 4:
                consulta_operador()
            if opcao == 5:
                from Menu import Menu
                Menu.menu()
            if opcao == 6:
                exit()
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print("=====Digite uma opção valida=====")
                operador()

        operador()

