from flask import Flask, render_template, request, jsonify, url_for, session, redirect
import json
import os

app = Flask(__name__)
app.secret_key = 'nfactorial-debatelink-login123'

USERS = {
    "admin@debatelink.org": "1lovedeb@telink"
}

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    program = request.form['program']
    message = request.form.get('message', '')

    entry = {
        'name': name,
        'email': email,
        'program': program,
        'message': message
    }

    file_path = 'data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

    return jsonify({'status': 'success'})


@app.route('/registrations')
def view_registrations():
    if 'user' not in session:
        return redirect(url_for('login'))
    try:
        with open('data.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    return render_template('registrations.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email in USERS and USERS[email] == password:
            session['user'] = email
            return redirect(url_for('view_registrations'))
        else:
            error = "You are not allowed access the data in this page."
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


