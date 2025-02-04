from flask import Flask
app=Flask(__name__)

@app.route('/')
def welcome():
    return "This is my first flask app"

@app.route('/root')
def root():
    return "This is my root page"

@app.route('/amit')
def Amit():
    return "Hello Amit"

app.run()