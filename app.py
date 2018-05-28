import display

from flask import Flask, request, json
app = Flask(__name__)

@app.route('/')
def hello_world():
    display.display('Hello Flask!')
    return 'Hello Flask!'

@app.route('/message', methods = ['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        display.display(request.data)
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        display.display(request.json['message'])
        return "JSON Message: " + json.dumps(request.json)

@app.route('/api/<text>')
def api_text(text):
    display.display(text)
    return text

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')