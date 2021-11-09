import twilio
from twilio.rest import Client
import random
import time

def otp_fun(tphone):
    try:
        otp = random.randint(1000,9999)
        account_sid = "**********************"
        auth_token = "*******************"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                body='Le code de vérification Tasbiq est le : ' + str(otp),
                from_='+18508209853',
                to=f'+212{tphone}'
            )
        
        time.sleep(5)
        return {"status" :True, "code":otp}
    except Exception as e:
        print(e)
        return {"status" :False, "code":otp}