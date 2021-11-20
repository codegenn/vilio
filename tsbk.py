from pyairtable import Table
from tsbk_requests import validateUser, createAdvance
from twillio_fun import otp_fun
from flask import Flask, session, redirect, url_for, request, render_template,flash

app = Flask(__name__)
app.debug = True

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

table_employes = Table('keygeraUQS9HeNE1Z', 'appVF9SXIP2f5vf5L', "Employes")
table_advances = Table('keygeraUQS9HeNE1Z', 'appVF9SXIP2f5vf5L', "Registre")



@app.route('/')
def index():
    if 'employe_id' in session and table_employes.get(session['employe_id']) != "None":
        user = table_employes.get(session['employe_id']) #load the user
        balance = round(user['fields']['Avance disponible'],2)
        return render_template('amount.html', name=user['fields']['Nom'],lastname=user['fields']['Prénom'],CIN=user['fields']['CIN'], balance = str(balance), form_url= url_for('request_advance'))
    else:
        return redirect(url_for('login'))


@app.route('/kyc', methods=['GET','POST'])
def kyc():
    try:
        res = session['res']
        print(session['phoneno'])
        fdigit = str(session['phoneno'])[0:4]
        ldigit = str(session['phoneno'])[-3:]
        tphone = fdigit +"***"+ldigit
        if request.method == 'POST':    
            otp = request.form['otp']
            try:
                if str(otp) == str(res['code']):
                    return redirect(url_for('index'))
                else:
                    flash("Entrez le code est invalide.")
            except:
                flash("Erreur de Twilio.")
                return render_template("KYC.html")

        return render_template("KYC.html",tphone = tphone)
    except:
        return redirect(url_for('login'))

@app.route('/resend',methods=['GET'])
def resend_otp():
    session['res'] = otp_fun(session['phoneno'])
    return redirect(url_for("kyc"))



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['firstname']
        rec = validateUser(name.upper(),lastname.upper(),request.form['cin'],request.form['tphone'],table_employes)
        if rec:
            if rec["status"]:
                session['employe_id'] = rec['data']['id']
                session['phoneno'] = request.form['tphone']
                session['res'] = otp_fun(session['phoneno'])
                return redirect(url_for("kyc"))
            else:
                flash(f"{rec['data']} : Ce numéro de téléphone n'est pas associé à cet utilisateur CIN.")
                return render_template('login.html')
        else:
            text = """Votre compte n’a pas encore été crée par votre
                    employeur. Veuillez contacter votre Responsable RH
                    pour plus d’informations"""
            return render_template('decline.html',msg=text)

    return render_template('login.html')
    
@app.route('/request_advance',methods=['GET','POST'])
def request_advance():
    user = table_employes.get(session['employe_id'])
    if request.method == 'POST':    
        try: 
            rec= createAdvance(user, float(request.form['amount']), table_advances )
        except:
            rec = False
    else:
        session.clear()
        text = "Erreur d'identification"
        return render_template('decline.html',msg=text)
    
    if rec:
        return render_template('confirm.html')
    else:
        session.clear()
        text = "Demande rejetée"
        return render_template('decline.html',msg=text)

if __name__=="__main__":
    app.run()