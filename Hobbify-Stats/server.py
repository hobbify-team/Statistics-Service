from flask import Flask
from flask import request
import querys
from datetime import date
import model


app = Flask(__name__)

@app.route('/')

def hello_world():
   # Connect to an existing database
   #querys.insertScore(2,date(2002, 12, 31),'Yoiky')
   
   
   return 'hola'

