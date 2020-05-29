#python3

from flask import Flask

# variable "app" within the dunder method of "(__name__)"
app = Flask (__name__)

#the below code is a decorator (provides additional functionalist to an existing object without modifying its structure)
# the "/" below is what is known as "root" directory or index. Changing this would result in a different url i.e. if you change it to "app" the url will be http://127.0.0.1:5000/App
@app.route('/')
def welcome():
    return "hello world, this is my first flask app"

# you can't have the same function name
@app.route('/page1')
def page1():
    return "this is my first page"

@app.route('/page2')
def page2():
    return "This is my second page"

#Main difference between POST and GET method is that GET carries request parameter appended in URL string while POST 
#carries request parameter in message body which makes it more secure way of transferring data from client to server 
#in http protocol. Basically, if you want a more secure connection, use "POST"
@app.route('/method', methods =['GET','POST'])
def method():
    if method == 'POST':
        return "you've used a post request."
    else:
        return  "You are using the Get Method"


# the code below will run the flask application
app.run()

