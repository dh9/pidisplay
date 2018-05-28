import display

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    display.display('Hello Flask from ubuntu!')
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')