
# Import Flask
from flask import Flask, request, session, redirect, url_for, abort
app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return('Hello, Home page!')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

# Logout page
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
