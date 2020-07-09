from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


#Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


#Database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inti db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)


#Endpoint GET
@app.route('/', methods=['GET'])

def fr():
    return jsonify({'message': 'endpoints get in use'})


#Run server 

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

