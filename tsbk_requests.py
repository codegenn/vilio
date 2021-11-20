import json
from pyairtable.formulas import match

def checkBalance(row):
    return (row['fields']['Avance disponible'])

def validateUser(name,firstname,cin,tphone,table):
    formula = match({"Nom":name.upper(),"Prénom":firstname.upper(),"CIN":cin.upper()})  
    data = json.loads(json.dumps(table.first(formula=formula)))                      
     #Parsing JSON Dummp from match response
    if data : 

        #KYC DE MERDE A CHANGER 
        # if kyc == data['fields']['Code KYC']:
        #     return(data)
        # else:
        #     print('KYC ERRONE')
        #     return(False)

        #Téléphone DE MERDE A CHANGER 
        if tphone == data['fields']['Téléphone']:
            # return(data)
            return {"status":True,"data":data}
        else:
            data = 'Téléphone ERRONE'
            return {"status":False,"data":data}
    else:
        print('Utilisateur erroné/inexistant')
        return(False)
def createRequest(data_employe,amount,table_request):
        try:
            req = table_request.create({"Nom et Prénom":[data_employe['id']],"Montant de l'avance": amount})
            return (req['id'])
        except:
            return(False)


def createAdvance(data_employe, amount, table_request ):
    if data_employe['fields']['Avance disponible'] > amount and data_employe['fields']['Statut']== ['Actif']:
        try: 
            rec=createRequest(data_employe,amount,table_request)
        except: 
            return False
        finally:
            return rec
    else:
        print('Fonds insufisant ou utilisateur inactif')
        return(False)