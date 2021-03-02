from flask import Flask, render_template,request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def dashboard():
    return 'hello'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()
