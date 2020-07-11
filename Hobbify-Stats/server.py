from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from model import array_score

#Init app
app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

#Database
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:password@127.0.0.1/hobbify_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inti db
login_manager = LoginManager(app)
login_manager.login_view = "login"
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)


#Endpoint GET
@app.route('/', methods=['GET'])

array_score()


#Run server 

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

