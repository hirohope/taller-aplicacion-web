from flask import Flask, render_template, request, redirect
import datetime

app = Flask("miAplicacion")

chatList = []

@app.route('/')
def index():
	return render_template("index2.html", comments = chatList)


@app.route('/chat', methods=['POST'])
def chat():
	if request.method == 'POST':
		chatList.insert(0,(datetime.datetime.now(), request.form['name'], request.form['comment']))
		print chatList
		return redirect('/')


if __name__ == "__main__":
	app.debug = True
	app.run()
