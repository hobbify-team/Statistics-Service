from flask import Flask
from flask import request
import querys
from datetime import date
from markupsafe import escape
import model


app = Flask(__name__)

@app.route('/heatmap/<username>')
def heatmap(username):
   # Connect to an existing database
   #querys.insertScore(2,date(2002, 12, 31),'Yoiky')  
   username = escape(username)
   data = model.array_score(username)
   # print(data)
   return  {
        "username": username,
        "Data": data        
    }

