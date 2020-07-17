from flask import Flask
import querys
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello_world():
   # Connect to an existing database
   #querys.insertScore(2,date(2002, 12, 31),'Yoiky')
   
   
   return 'hola'

