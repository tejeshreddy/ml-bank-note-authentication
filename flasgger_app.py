from flask import Flask, request
import pickle
import sklearn
import pandas as pd
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Loading the pickle file
pickle_file = open("pickle_model.pkl", "rb")
classifier = pickle.load(pickle_file)


@app.route("/")
def home():
    return "Welcome!"

@app.route("/predict")
def predict_single_entry():
    """Bank Note Authentication
    ---
    parameters:
        - name: variance
          in: query
          type: number
        - name: skewness
          in: query
          type: number
        - name: curtosis
          in: query
          type: number
        - name: entropy
          in: query
          type: number
          require: true
    responses:
        200:
            description: The output values
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    
    return str(classifier.predict([[variance, skewness, curtosis, entropy]]))

@app.route("/predict_file", methods=["POST"])
def predict_file():
    """Bank note authentication
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true

    responses:
        200:
            description: The output value
    """
    test_file = request.files.get("file")
    df = pd.read_csv(test_file)
    
    return str(classifier.predict(df))
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")
    