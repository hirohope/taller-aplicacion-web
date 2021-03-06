from flask import Flask
import os

app = Flask("miAplicacion")

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello/')
def hello():
	return 'Hello World'

from flask import request
@app.route('/goodbye')
def goodBye():
	return 'Good Bye, {}'.format(request.args['name'])

@app.route('/hello/<name>')
def helloName(name="Nobody"):
	return 'Hello, {}'.format(name)


if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)