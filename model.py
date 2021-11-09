from pyairtable.orm import Model, fields

class Employe(Model):
    name = fields.TextField("Nom")
    lastname = fields.TextField("Prénom")
    cin = fields.TextField("CIN")
    phone = fields.TextField("Téléphone")
    entreprise = fields.TextField("Entreprise")
    dob = fields.TextField("Date de naissance")
    

    class Meta:
        base_id = "appVF9SXIP2f5vf5L"
        table_name = "Employes"
        api_key = "keygeraUQS9HeNE1Z"



class Entreprise(Model):
    name = fields.TextField("Name")
    employes = fields.LinkField("Employés", Employe, lazy = False)
    class Meta:
        base_id = "appVF9SXIP2f5vf5L"
        table_name = "Entreprise"
        api_key = "keygeraUQS9HeNE1Z"


    
class Registre(Model):
    employe = fields.LinkField("Nom et Prénom", Employe, lazy=False)
    advance = fields.IntegerField("Montant de l'avance")
    class Meta:
        base_id = "appVF9SXIP2f5vf5L"
        table_name = "Registre"
        api_key = "keygeraUQS9HeNE1Z"