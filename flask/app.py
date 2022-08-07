from flask import Flask, render_template, url_for, request, redirect, make_response
from datetime import datetime
from tasks import ToDo
from users import users

users = users()
todo = ToDo()

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    username = request.cookies.get('login')
    print(username)
    if username == None:
        return render_template("login.html")
    if request.method == 'POST':
        task_content = request.form['content']
        if task_content == "":
            lista = todo.fetch_task(username)
            homework = todo.fetch_homework(username)
            notes = todo.fetch_notes(username)
            return render_template("index.html", tasks=lista, homework=homework, notes=notes, username=username)
        msg = todo.add_task(task_content, str(datetime.now())[:-7], username)
        lista = todo.fetch_task(username)
        homework = todo.fetch_homework(username)
        notes = todo.fetch_notes(username)
        return render_template("index.html", tasks=lista, homework=homework, notes=notes, username=username)
    else:
        lista = todo.fetch_task(username)
        homework = todo.fetch_homework(username)
        notes = todo.fetch_notes(username)
        return render_template("index.html", tasks=lista, homework=homework, notes=notes, username=username)

@app.route("/add-homework", methods=['POST', 'GET'])
def add_homework():
    username = request.cookies.get('login')
    print(username)
    homework_name = request.form['name']
    homework_subject = request.form['subject']
    homework_when = request.form['when']
    if homework_when == "" or homework_subject == "" or homework_name == "":
        return redirect('/')
    todo.add_homework(homework_name, homework_subject, homework_when, username)
    return redirect('/')

@app.route("/add-note", methods=['POST', 'GET'])
def add_note():
    username = request.cookies.get('login')
    print(username)
    note_name = request.form['name']
    if note_name == "":
        return redirect('/')
    todo.add_note(note_name, username)
    return redirect('/')

@app.route("/delete/<id>")
def delete(id):
    username = request.cookies.get('login')
    print(username)
    todo.delete_task(id, username)
    return redirect('/')

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    username = request.cookies.get('login')
    print(username)
    note_name = id
    notes = todo.fetch_notes(username)
    print(note_name)
    if request.method == 'POST':
        note_content = request.form['content']
        print(note_name)
        try:
            print(note_content, note_name)
            todo.update_note(note_content, note_name, username)
            return redirect('/')
        except Exception as err:
            return str(err)
    else:
        return render_template('update.html', note=notes[id], note_name=id)

@app.route("/delete_homework/<id>")
def delete_homework(id):
    username = request.cookies.get('login')
    print(username)
    todo.delete_homework(id, username)
    return redirect('/')

@app.route("/delete_note/<id>")
def delete_note(id):
    username = request.cookies.get('login')
    print(username)
    todo.delete_note(id, username)
    return redirect('/')

@app.route("/login", methods=['GET', 'POST'])
def login():
    res = make_response(redirect('/'))
    print(request.form)
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if request.form.get('button') == 'create-account':
            msg = users.create_account(login, password)
            if msg != "done":
                return str(msg)
            return render_template("login.html")
        msg = users.check_login(login, password)
        print(msg)
        if msg == True:
            res.set_cookie('login', 'lol', max_age=0)
            res.set_cookie('login', login)
            return res
        if msg != True:
            return str(msg)
        return res
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)