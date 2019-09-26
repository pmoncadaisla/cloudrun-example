import time

from flask import Flask

app = Flask(__name__)



@app.route('/')
def hello():
    message = 'Hello Keepcoding! from Cloud Run! Last day :-('
    print('{"message": "'+message+'"}')
    return message

