from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from controllers import helloController
from flask_sqlalchemy import SQLAlchemy
from data_processing import data_processor


app = Flask(__name__)

api = Api(app)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.route('/foo', methods=['POST','OPTIONS'])
cross_origin(origin='*',headers=['Content-Type','Authorization'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

api.add_resource(helloController.HelloController, '/api/predict')

if __name__ == '__main__':
    app.run(debug=True)
