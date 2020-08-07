#!/usr/bin/env python
"""This script is where the API paths and their behavior are declared"""
from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import model
app = Flask(__name__)
@app.route('/', methods=['GET'])
def req():
    """ This function consults the Score of each user """
    info = request.get_json()
    username = info['username']
    date = info['date']
    info = model.array_score(username, date)
    return jsonify({'username':username, 'list_score':info})

@app.route('/', methods=['POST'])
def up_score():
    """ This function calculates the relative frequency each time it is called from the frontend """
    try:
        status_code = Response(status=201).status_code
        info = request.get_json()
        username = info['username']
        date = info['date']
        model.relative_freq(username, date)
        return jsonify({'username':username, 'status':status_code})
    except TypeError:
        print("[Error] ", TypeError.__str__())
        return jsonify({'Status': 'Please review info body'})
