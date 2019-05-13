from __future__ import division
from flask import Flask, request
from flask_restful import Resource
from sklearn import preprocessing
from sklearn import metrics
from sklearn.model_selection import train_test_split #to split in train and test set
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
from sklearn import preprocessing
from data_processing import data_processor
from ast import literal_eval
from sklearn.externals import joblib


class HelloController(Resource):

    def get(self):
        return {"response" : data_processor()} 
    
    def post(self):
        content = request.json
        return {"result" : data_processor(content["landmarks"])}

    def put(self):
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}
