from flask import Flask, render_template, request, redirect

app = Flask("miAplicacion")

chatList = []

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
	if request.method == 'POST':
		chatList.append(request.form['comment'])
		print chatList
		return redirect('/')


if __name__ == "__main__":
	app.debug = True
	app.run()