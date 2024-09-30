from flask import Flask, render_template, request

app = Flask(__name__)

# A dictionary to store tasks with an ID
tasks = {}
task_id_counter = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global task_id_counter
    response_text = ""

    if request.method == 'POST':
        if 'add_task' in request.form:
            task_content = request.form.get('task_content')
            if task_content:
                tasks[task_id_counter] = task_content
                task_id_counter += 1

        elif 'delete_task' in request.form:
            task_id_to_delete = int(request.form.get('task_id_to_delete'))
            tasks.pop(task_id_to_delete, None)

        
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    # app.run(port=5000,debug=True)
    app.run(host='0.0.0.0',port=5000,debug=True)
