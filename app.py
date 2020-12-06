import os
from flask import Flask, jsonify
from flask import request
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)
minioClient = Minio(endpoint='minio:9000',
	                    access_key='AKIAIOSFODNN7EXAMPLE',
	                    secret_key='wJalrXUtnFEMIK7MDENGbPxRfiCYEXAMPLEKEY',
	                    secure=False)
	
#we define the route /
@app.route('/')
def welcome():
	filename = "finalized_model2.pkl"
	x = request.args.get('x')
	# Initialize minioClient with an endpoint and access/secret keys.
	data = minioClient.fget_object(bucket_name="pickle", object_name="finalized_model2.pkl", file_path="finalized_model2.pkl")
	predictor2 = pickle.load(open(filename, 'rb'))
	outcome = predictor2.predict(X=[[int(x)]])[0]
	return jsonify({'value': outcome})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=1234)