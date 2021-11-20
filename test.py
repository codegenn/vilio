import json
from pyairtable import Table
from pyairtable.formulas import match

table_employes = Table('keygeraUQS9HeNE1Z', 'appVF9SXIP2f5vf5L', "Employes")


# for i in table_employes.all():
#     print(i["fields"]["Nom"])
print(table_employes.first(formula=match({"Nom":" RABENATOANDRO"})))
# formula = match({"Nom":name.upper(),"Prénom":firstname.upper(),"CIN":cin.upper()})  
# data = json.loads(json.dumps(table.first(formula=formula))) 