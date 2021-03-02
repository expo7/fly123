from flask import Flask, render_template,request
import robin_stocks as rs 
def sign_in():
    rs.robinhood.login(username='bsavelli66@gmail.com', password='Canyon6687', 
                          expiresIn=86400, scope='internal', by_sms=True,
                          store_session=True)


app = Flask(__name__)

@app.route('/')
def dashboard():
    sign_in()
    order=rs.robinhood.order_buy_crypto_by_price('BTC',5)
    return order 

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()
