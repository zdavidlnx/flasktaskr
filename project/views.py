# project/views.py

import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, url_for, request, session, g


# Configuración

app = Flask(__name__)
app.config.from_object('_config')


# helpers

def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            redirect(url_for('login'))

    return wrap


# Route handlers
@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('Goodbye!!')
    redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            flash('Welcome!!')
            return redirect(url_for('tasks'))
    return render_template('login.html')


@app.route('/tasks/')
@login_required
def tasks():
    g.db = connect_db()
    cursor = g.db.execute('SELECT name, due_time, priority, task_id FROM tasks WHERE status=1')

    # genero un array de diccionarios, cada dicionario es una fila
    open_tasks = [dict(name=row[0], due_time=row[1], priority=row[2], task_id=row[3]) for row in cursor.fetchall()]

    cursor = g.db.execute('SELECT name, due_time, priority, task_id FROM tasks WHERE status=0')

    # genero un array de diccionarios, cada dicionario es una fila
    closed_tasks = [dict(name=row[0], due_time=row[1], priority=row[2], task_id=row[3]) for row in cursor.fetchall()]
    g.db.close()

    return render_template('tasks.html',
                           form=AddTaskForm(request.form),
                           open_tasks=open_tasks,
                           closed_tasks=closed_tasks)



