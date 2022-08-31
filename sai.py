from flask import Flask,redirect,url_for,render_template

app =Flask(__name__)

@app.route('/')
def welcome():
    return "welcome sai"

@app.route('/sucess/<int:score>')
def sucess(score):
    return "the person has passed and the marks is " +str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is " +str(score)
#result cheker
@app.route('/result/<int:score>')
def result(score):
    results = ""
    if score<50:
        results ="fail"
    else:
        results = "sucess"
    return redirect(url_for(results,score = score))
    


if __name__ == "__main__":
    app.run(debug=True)