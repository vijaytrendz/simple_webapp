from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, it is a new web page/app!!!"
    
    ###Testing