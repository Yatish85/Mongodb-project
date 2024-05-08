from flask import Flask,render_template,request
from pymongo import MongoClient
app=Flask("__name__")
client=MongoClient("mongodb://localhost:27017/")
db=client["school"]
collecti=db["students"]
@app.route("/")
def index():
    return render_template("studentdetails.html")
@app.route("/submit",methods=["POST"])
def submit():
    student={
        'name':request.form['username'],
        'age':int(request.form['age']),
        'class':request.form['class'],
        'hindi':int(request.form['subject']),
        'english':int(request.form['subject']),
        'math':int(request.form['subject']),
        'science':int(request.form['subject']),
        'information_technology':int(request.form['subject'])
    }
    collecti.insert_one(student)

    if student['hindi']>=33 and student['english']>=33 and student['science']>=33 and student['math']>=33 and student['information_technology']>=33:
        result = "Congratulations! You are passed and promoted to the next class."
    else:
        result = "Sorry, you are failed."

    return result

if __name__=="__main__":
    app.run(debug=True)