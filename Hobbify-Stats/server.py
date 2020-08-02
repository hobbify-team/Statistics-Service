from flask import Flask
from flask import request
from flask import jsonify
import querys
from datetime import date
from markupsafe import escape
import model



app = Flask(__name__)

@app.route('/' , methods=['GET'] )   

def req():

   info = request.get_json()
   username = info['username']
   date = info['date']
   
   info = model.array_score(username, date)

   return jsonify({'username' : username ,  'list_score': info  })

