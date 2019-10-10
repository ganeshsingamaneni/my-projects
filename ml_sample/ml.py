from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
from app import *
# Your API definition
# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         lr = joblib.load("model.pkl") # Load "model.pkl"
#         print ('Model loaded')
#         model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
#         print ('Model columns loaded')
#         if lr:
#             json_ = request.json
#             print(json_)
#             query = pd.get_dummies(pd.DataFrame(json_))
#             query = query.reindex(columns=model_columns, fill_value=0)

#             prediction = list(lr.predict(query))

#             return jsonify({'prediction': str(prediction)})

#         else:
#             print ('Train the model first')
#             return ('No model here to use')
#     except:

#             return jsonify({'trace': traceback.format_exc()})    

# if __name__ == '__main__':
#     try:
#         port = int(sys.argv[1]) # This is for a command-line input
#     except:
#         port = 12345 # If you don't provide any port the port will be set to 12345
