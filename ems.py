# --*-- coding:utf-8 --*--

from flask import Flask, request
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    return '<h1>your browser is {}</h1>'.format(user_agent)

if __name__ == '__main__':
    app.run(debug=True)
