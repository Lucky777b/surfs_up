# Import Dependencies 
import datetime as dt
import numpy as np
import pandas as pd
# Import SQLAlchemy dependencies to access data in SQLite database 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Import dependency needed for Flask
from flask import Flask, jsonify

# Set up engine to access and query SQLite Database file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect database into classes 
Base = automap_base()
# use PythonFlask fcn to reflect the tables 
Base.prepare(engine, reflect=True)
# save references to each table and create variable for each of classes to reference later 
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create session link from Python to our database
session = Session(engine)

# Set up Flask 
# define Flask app and call it 'app'
app = Flask(__name__)
# define the welcome route 
@app.route("/")

# Create fcn welcome() with a return statement
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

