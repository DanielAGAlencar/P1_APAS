import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbtraportadora"]
mycolOperador = mydb["operador"]
mycolAgencia = mydb["agencia"]


import re


class Regex:

    def valida_id(id):
        if not re.fullmatch(r"\d{0,9}", id):
            print("Id Invalido")
            return True
        else:
            return False

    def valida_tel(tel):
        if not re.fullmatch(r"(\(?\d{2}\)?\s?\-?\s?)?(\d{4,5}\-?\d{4})", tel):
            print("Telefone invalido!")
            return True
        else:
            return False

    def valida_cpf(cpf):
        if not re.fullmatch(r"(\d{3}\.?)(\d{3}\.?)(\d{3}\-?)(\d{2})", cpf):
            print("CPF invalido!")
            return True
        else:
            return False

    def valida_cnpj(cnpj):
        if not re.fullmatch(r"(\d{2}\.?)(\d{3}\.?)(\d{3}\/?)(\d{4}\-?)(\d{2})", cnpj):
            print("CNPJ invalido!")
            return True
        else:
            return False

    def valida_n_matricula(n):
        if not re.fullmatch(r"\d{5,10}", n):
            print("Numero de Matricula invalido!")
            return True
        else:
            return False

    def valida_valores(valor):
        if not re.fullmatch(r"(\d{1,3}\.)?(\d{1,3}\.)?(\d{1,3}\.)?(\d{1,3}\,)(\d{2})", valor):
            print("Valor Invalido!")
            return True
        else:
            return False