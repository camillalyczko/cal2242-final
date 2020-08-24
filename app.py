# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: camilla
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/favorite_site")
def favorite_site():
    return render_template("favsite.html")

#@app.route("my_assignments")
#def my_assignments():
    #return 

@app.route("/my_classes")
def my_classes():
    return render_template("classes.html")

#start the server
if __name__ == "__main__":
    app.run()