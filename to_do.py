from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def give_task():
        Task1=''
        Task2=''
        Task3=''
        Task4=''
        if request.method =='POST' and 'Task1' in request.form:
                Task1=request.form.get('Task1')
                Task2=request.form.get('Task2')
                Task3=request.form.get('Task3')
                Task4=request.form.get('Task4')
        return render_template("to_do.html",Task1=Task1,Task2=Task2,Task3=Task3,Task4=Task4)
@app.route('/display', methods=['GET'])
def see_task():
    Task1=''
    Task2=''
    Task3=''
    Task4=''
    if request.method =='POST' and 'Task1' in request.form:
                Task1=request.form.get('Task1')
                Task2=request.form.get('Task2')
                Task3=request.form.get('Task3')
                Task4=request.form.get('Task4')
    return render_template("to_do.html",Task1=Task1,Task2=Task2,Task3=Task3,Task4=Task4)
    
app.run()
