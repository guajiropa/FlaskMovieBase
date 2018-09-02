"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/listing')
def listing():
    return 0 


@app.route('/comments')
def comments():
    return 0


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
