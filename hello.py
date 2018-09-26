
from flask import Flask 
from flask import request


app = Flask(__name__)

PEOPLE= []
@app.route('/')
@app.route('/index')
def index():
    name = request.args.get("name", "Samwise")
    PEOPLE.append(name)
    return "Hello, %s I have seen: %s before you!" % (name, ", ".join(PEOPLE))

@app.route("/guess")
def guess():
    return "You guessed: %s" % (request.args.get("letter"))
