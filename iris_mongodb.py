#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:14:22 2019

@author: nicolas
"""

from pymongo import MongoClient
import pandas as pd

class IrisMongoDB:
    def getCollection(self):
        client = MongoClient()
        db = client['iris']
        collection = db['iris']
        
        return collection
    
    def getDataframe(self):
        collection = self.getCollection()
        cursor = collection.find({},{'_id':0})
        dataframe = pd.DataFrame(list(cursor))
        
        print(dataframe.head(5))
        
        return dataframe
    
    def printData(self):
        collection = self.getCollection()
        cursor = collection.find()
        for doc in cursor:
            sepal_length = doc['sepal_length']
            category = doc['category']
            print(sepal_length, category)
            
iris = IrisMongoDB()
iris.printData()            