from flask import Flask, request
import pickle
import sklearn
import pandas as pd

app = Flask(__name__)

# Loading the pickle file
pickle_file = open("pickle_model.pkl", "rb")
classifier = pickle.load(pickle_file)


@app.route("/")
def home():
    return "Welcome!"

@app.route("/predict")
def predict_single_entry():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    
    return str(classifier.predict([[variance, skewness, curtosis, entropy]]))

@app.route("/predict_file", methods=["POST"])
def predict_file():
    test_file = request.files.get("file")
    df = pd.read_csv(test_file)
    
    return str(classifier.predict(df))
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    