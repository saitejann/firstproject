from flask import Flask 

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to My Youtube Channel please subscribe to my chanlel"

@app.route('/members')
def members():
    return " another function"


if __name__ == "__main__":
    app.run(debug=True)

