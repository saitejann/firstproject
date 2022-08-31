##integrate HTML with flask 
##HTTP verb GET and POST

##jinga2 template engine
'''
{%...%} for conditinal statements
{{ }} expressions to print output
{# #} this is for comments

'''


from flask import Flask,redirect, render_template,url_for,request

app =Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/sucess/<int:score>')
def sucess(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}
  
    return render_template('result.html',result=exp)

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
    
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science = float(request.form['Science'])
        maths  = float(request.form["Maths"])
        DataScience=float(request.form["DataScience"])
        total_score=(science+maths+DataScience)/3

    
        res="sucess"
    return redirect(url_for(res,score=total_score))



##result checker html page

if __name__ == "__main__":
    app.run(debug=True)