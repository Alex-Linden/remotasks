from flask import Flask, redirect, url_for, session
from facebook import GraphAPI

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['FACEBOOK_APP_ID'] = 'your_app_id'
app.config['FACEBOOK_APP_SECRET'] = 'your_app_secret'

@app.route('/')
def index():
    if 'facebook_token' in session:
        graph = GraphAPI(session['facebook_token'])
        # graph.put_object(parent_object='me/feed', connection_name='feed', message='Your post message')
        graph.put_comment(object_id='post_id', message='Your comment message')
        return 'Post published successfully!'
    else:
        return redirect(url_for('login'))

# Other routes for login and callback as shown in the previous example...

if __name__ == '__main__':
    app.run(debug=True)
