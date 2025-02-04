from flask import Flask, request

app = Flask(__name__)

tasks = []  # Global list to store tasks

@app.route('/', methods=['POST'])
def give_task():
    data = request.json  # Expecting JSON input
    task = data.get("task")  # Get task from JSON body
    
    if task:
        tasks.append(task)
        return f"Task added successfully."

@app.route('/display', methods=['GET'])
def see_task():
    if tasks:
        return "Tasks: " + ", ".join(tasks)
    return "No tasks available"
    
app.run()
