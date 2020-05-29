#python3

from flask import Flask

# variable "app" within the dunder method of "(__name__)"
app = Flask (__name__)

#the below code is a decorator (provides additional functionalist to an existing object without modifying its structure)
@app.route('/')
def welcome():
    return "hello world, this is my first flask app"




# the code below will run the flask application
app.run()

