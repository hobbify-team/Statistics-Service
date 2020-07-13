from flask import Flask
from flask import request
import querys
from datetime import date
import model


app = Flask(__name__)

@app.route('/')
def graph():
    username = request.args.get('username','no existe el usuario')
    print(model.array_score('Yoiky'))
    return 'Ok dictionary'



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
