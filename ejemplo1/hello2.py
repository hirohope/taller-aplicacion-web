from flask import Flask

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
	return 'Good Bye, %s' % (request.args['name'])

@app.route('/hello/<name>')
def helloName(name="Nobody"):
	return 'Hello, %s' % name

if __name__ == "__main__":
	app.debug = True
	app.run()