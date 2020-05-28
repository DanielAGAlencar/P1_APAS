import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbtraportadora"]
mycolOperador = mydb["operador"]
mycolAgencia = mydb["agencia"]
mycolCliente = mydb["cliente"]
myquery = {'relacao_agencia.cnpj_agencia': '34343434' }
#myquery = {'relacao_agencia': {'cnpj_agencia': '34343434', 'nome_agencia': {"$regex": 'agencia teste'}}}
#myquery = {"nome": {"$regex":"da"}}
i = 1
for x in mycolOperador.find(myquery, {"_id":0, "id": 1}):
  print(x)
  y = (str(x).replace("{'id': '", ''))
  n = (y.replace("'}", ''))
  nn = (int(n))
  if i < nn:
    i = nn
  else:
    i = i
print(i+1)
  #y = (str(x).replace("{'nome': '", ''))
  #nome = (y.replace("'}",''))
  #print(nome)
#print(nome)