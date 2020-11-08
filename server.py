from bottle import Bottle, route, run, response, static_file
from os import path as os_path


app = Bottle()

@app.route('/')
def index():
	return static_file('index.html', root='static')

@app.route('/about')
def about():
	return static_file('pages/about.html', root='static')

@app.route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root='static')


@app.route('/success', method='GET')
def server_success():
	return "success! success! success!"

@app.route('/fail', method='GET')
def server_fail():
	raise RuntimeError("There is an error!")
	return "fail! fail! fail!"


if __name__ == "__main__":
	app.run(host='localhost', port=8080, debug=True)
