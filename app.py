from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Well done Bill Be more creative a!'
