# Put your app in here.
from flask import Flask, request
from operations import add,sub,mult,div,square

app = Flask(__name__)


@app.route("/add")
def do_add():
    """add a and b parameters from the URL"""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route("/sub")
def do_sub():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route('/mult')
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)


@app.route('/square')
def do_square():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  square(a,b)
    return str(result)



operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
    "square": square
}

@app.route('/math/<parameter>')
def do_math(parameter):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[parameter](a, b)
    return str(result)
