from flask import Flask, render_template

@app.route("/hello2/<string:name_to_greet>/")
def hello2(name_to_greet):
 return render_template('hello.html', person_to_greet=name_to_greet)