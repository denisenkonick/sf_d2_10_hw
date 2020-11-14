from bottle import Bottle, route, HTTPResponse, static_file
import os
import sentry_sdk

app = Bottle()

@app.route('/')
def index():
    form = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>D2 Denisenko</title>
        <link rel="stylesheet" href="/static/style.css" type="text/css">
    </head>
    <body>
        <h1>This is main page</h1>
        <hr>
        <h2>For visit successful page, append to the end of URL "https://young-journey-39325.herokuapp.com<span style="color: lawngreen;">/success</span>"</h2>
        <hr>
        <h2>For visit fail page, append to the end of URL "https://young-journey-39325.herokuapp.com<span>/fail</span>"</h2>
        <hr>
    </body>
</html>
"""
    return form


@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static')

@app.route('/success', method='GET')
def server_success():
    return HTTPResponse(status=200, body="Successful page")

@app.route('/fail', method='GET')
def server_fail():
    raise RuntimeError("There is an error!")
    return HTTPResponse(status=500, body="Fail page")

if os.environ.get("APP_LOCATION") == "heroku":
    sentry_sdk.init(dsn=os.environ['SENTRY_DSN'],
                    integrations=[BottleIntegration()]
                    )
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3,
    )
elif __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
    
