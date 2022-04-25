from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome to my Hompage'
    
@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"
