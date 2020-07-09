from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


#Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


#Database
app.config['SQLALCHEMY_DATABASE_URL']= 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inti db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)


#Endpoint GET
@app.route('/', methods=['GET'])

def get():
    return jsonify({'message': 'endpoints get in use'})

#Endpoint POST
@app.route('/users', methods=['POST'])

def post():
     pass


#Run server 

if __name__ == '__main__':
    app.run(debug=True)