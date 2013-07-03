from flask import Flask, render_template, request, redirect

app = Flask("miAplicacion")

chatList = []

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/chat', methods=['GET', 'POST'])
def chat():
	if request.method == 'POST':		
		return "ok: %s" % (request.form['comment'])
	return "hola"

if __name__ == "__main__":
	app.debug = True
	app.run()