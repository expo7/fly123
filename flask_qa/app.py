from flask import Flask, render_template,request
import robin_stocks as rs 
import pyotp
def sign_in():
    totp  = pyotp.TOTP("X332CR3PQSYGYOF7").now()
    login = rs.robinhood.login('bsavelli66@gmail.com',password='Canyon6687', mfa_code=totp)
        


app = Flask(__name__)

@app.route('/')
def dashboard():
    sign_in()
    order=rs.robinhood.order_buy_crypto_by_price('BTC',5)
    return order 

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()
 