from flask import Flask

# create a new Flask app instance 
app = Flask(__name__)

# create Flask route
    # define starting point aka 'root'
@app.route('/')

# create fcn called hello_world()
    # whenever make route in Flask, you put code you want in that specific route below @app.route()
def hello_world():
    return 'Hello World'