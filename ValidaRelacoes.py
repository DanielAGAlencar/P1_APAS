import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbtraportadora"]
mycolOperador = mydb["operador"]
mycolAgencia = mydb["agencia"]
mycolCliente = mydb["cliente"]
mycolCadStatus = mydb["cadstatus"]

class ValidaRelacoes:

    def valida_cnpj_agencia(cnpj):
        myquery = {"cnpj": cnpj}
        i = False
        for x in mycolAgencia.find(myquery):
            i = True
        if i == True:
            return False
        else:
            print("CNPJ invalido!")
            return True

    def valida_cnpj_agencia_cad(cnpj):
        myquery = {"cnpj": cnpj}
        i = False
        for x in mycolAgencia.find(myquery):
            i = True
        if i == True:
            print("CNPJ já cadastrado!")
            return True
        else:
            return False

    def preenche_nome_agencia(cnpj):
        myquery = {"cnpj": cnpj}
        for x in mycolAgencia.find(myquery, {"_id":0, "nome": 1 }):
            y = (str(x).replace("{'nome': '",''))
            nome = (y.replace("'}",''))
        return nome

    def valida_n_matricula_operador(n_matricula):
        myquery = {"n_matricula": n_matricula}
        i = False
        for x in mycolOperador.find(myquery):
            i = True
        if i == True:
            return False
        else:
            print("Numero de Matricula invalodo!")
            return True

    def valida_n_matricula_operador_cad(n_matricula):
        myquery = {"n_matricula": n_matricula}
        i = False
        for x in mycolOperador.find(myquery):
            i = True
        if i == True:
            print("Numero de Matricula já cadastrado!")
            return True
        else:
            return False

    def preenche_nome_operador(n_matricula):
        myquery = {"n_matricula": n_matricula}
        for x in mycolOperador.find(myquery, {"_id":0, "nome": 1 }):
            y = (str(x).replace("{'nome': '",''))
            nome = (y.replace("'}",''))
        return nome

    def valida_cpf_operador_cad(cpf):
        myquery = {"cpf": cpf}
        i = False
        for x in mycolOperador.find(myquery):
            i = True
        if i == True:
            print("CPF já cadastrado!")
            return True
        else:
            return False

    def valida_cpf_cliente(cpf):
        myquery = {"cpf": cpf}
        i = False
        for x in mycolCliente.find(myquery):
            i = True
        if i == True:
            return False
        else:
            print("CPF invalodo!")
            return True

    def valida_cpf_cliente_cad(cpf):
        myquery = {"cpf": cpf}
        i = False
        for x in mycolCliente.find(myquery):
            i = True
        if i == True:
            print("CPF já cadastrado!")
            return True
        else:
            return False

    def preenche_nome_cliente(cpf):
        myquery = {"cpf": cpf}
        for x in mycolCliente.find(myquery, {"_id":0, "nome": 1 }):
            y = (str(x).replace("{'nome': '",''))
            nome = (y.replace("'}",''))
        return nome

    def valida_id_status(id):
        myquery = {"id": id}
        i = False
        for x in mycolCadStatus.find(myquery):
            i = True
        if i == True:
            return False
        else:
            print("Id invalido!")
            print("Lista de status válidos: ")
            mydoc = mycolCadStatus.find({}, {"_id":0, "id": 1, "descricao": 1} ).sort("id", 1)
            for x in mydoc:
                i = (str(x).replace("{'descricao': '", 'Descrição: '))
                j = (i.replace("', 'id': '", ' - ID: '))
                h = (j.replace("'}", ''))
                print(h)
            return True

    def preenche_desc_status(id):
        myquery = {"id": id}
        for x in mycolCadStatus.find(myquery, {"_id":0, "descricao": 1 }):
            y = (str(x).replace("{'descricao': '",''))
            descricao = (y.replace("'}",''))
        return descricao