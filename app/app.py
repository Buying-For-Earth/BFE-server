import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
	return 'hello! cicd is working!!! WA! '

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
