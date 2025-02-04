from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

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