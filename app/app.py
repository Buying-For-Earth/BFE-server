import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
<<<<<<< HEAD
	return 'hello! cicd is working!!!'
=======
	return 'hello!'
>>>>>>> 0520fe3c0e4a7d0deb85371828c0b7ea963ca0ad

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)