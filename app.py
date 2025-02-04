from flask import Flask,request
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

@app.route('/methods',methods=['GET','POST'])
def method():
    if request.method=='POST':
        return "You are using post"
    else:
        return"You are using Get"
app.run()