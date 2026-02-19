from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body {
                background-color: blue;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 20%;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>
    """