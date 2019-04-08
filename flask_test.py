#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:51:16 2019

@author: nicolas
"""

from flask import Flask, jsonify
from iris_mongodb import IrisMongoDB
from flask_cors import CORS #iNVESTIGAR


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    message = {'id':123,'name':'Flask test'}  
    return jsonify(message)

@app.route('/mongodb')
def mongodb():
    iris_mongodb = IrisMongoDB()
    dataframe = iris_mongodb.getDataframe()
    #data_json = dataframe.to_json(orient='records')
    #return jsonify(data_json)

    json_data = []
    for index, row in dataframe.iterrows():
        pl = row['petal_length']
        pw = row['petal_width']
        sl = row['sepal_length']
        sw = row['sepal_width']
        category = row['category']
       # item = [pl ,pw, sl, sw]
        #category = model.predict([item])[0]
        json_item = {'pl':pl, 'pw':pw, 'sl':sl, 'sw':sw, 'class':category}
        json_data.append(json_item)
    
    return jsonify(flowers=json_data)

if __name__ == '__main__':
   app.run()