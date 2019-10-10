from flask import Flask
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"
@app.route('/predict', methods=['POST'])
def predict():
    # try:
    lr = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')
    if lr:
        json_ = request.get_json()
        query = pd.get_dummies(pd.DataFrame(json_['data']))
        query = query.reindex(columns=model_columns, fill_value=0)

        prediction = list(lr.predict(query))

        return jsonify({'prediction': str(prediction)})

    else:
        print ('Train the model first')
        return ('No model here to use')
    # except:

    #         return jsonify({'trace': traceback.format_exc()})    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)