#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 06:29:50 2019

@author: nicolas
"""

from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

if __name__=="__main__":
    app.run()