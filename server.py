from bottle import Bottle, route, run, response, static_file
import os
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


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
