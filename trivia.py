import os
import ConfigParser
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Configuration
config = ConfigParser.RawConfigParser()
try:
    config.read('trivia.config')
except:
    config.read('trivia.config.default')


# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, config.get('trivia','database')),
    SECRET_KEY=config.get('trivia','secret_key'),
    USERNAME=config.get('trivia','admin_user'),
    PASSWORD=config.get('trivia','admin_pass')
))
app.config.from_envvar('TRIVIA_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    print app.config['DATABASE']
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource(os.path.join(app.root_path, 'schema.sql'), mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select * from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into entries (user, cwid, pin, q0, q1, q2, q3, q4, q5, q6, q7, q8, q9) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 [request.form['user'],
                 request.form['cwid'],
                 request.form['pin'],
                 request.form['q0'],
                 request.form['q1'],
                 request.form['q2'],
                 request.form['q3'],
                 request.form['q4'],
                 request.form['q5'],
                 request.form['q6'],
                 request.form['q7'],
                 request.form['q8'],
                 request.form['q9']])
    db.commit()
    flash('Submission Successfully Sent')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
