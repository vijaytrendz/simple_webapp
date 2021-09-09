from flask import *

app = Flask(__name__)

@app.route("/")
def message():

    return "<html><body><h1>Welcome to version 1 of this webpage</h1></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=true)