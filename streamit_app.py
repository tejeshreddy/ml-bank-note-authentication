import pickle
import sklearn
import pandas as pd
import streamlit as st

# Loading the pickle file
pickle_file = open("pickle_model.pkl", "rb")
classifier = pickle.load(pickle_file)

def home():
    return "Welcome!"

def predict_single_entry(variance, skewness, curtosis, entropy):
    return str(classifier.predict([[variance, skewness, curtosis, entropy]]))

def predict_file():
    test_file = request.files.get("file")
    df = pd.read_csv(test_file)
    
    return str(classifier.predict(df))

def main():
    st.title("Bank Note Authenticaion")
    html_template = """
        <div style="backgroud-color:tomato; padding:10px">
            <h2 style="color:white; text-align:center;">Streamlit Bank Authenticator ML App</h2>
        </div>
    """
    
    st.markdown(html_template, unsafe_allow_html=True) # To render the HTML contents
    
    # Taking all the user inputs
    variance = st.text_input("Variance", "Enter the variance here!")
    skewness = st.text_input("Skewness", "Enter the skewness here!")
    curtosis = st.text_input("Curtosis", "Enter the curtosis here!")
    entropy = st.text_input("Entropy", "Ente the entropy here!")
    
    if st.button("Predict"):
        result = predict_single_entry(variance, skewness, curtosis, entropy)
        st.success(result)
    
if __name__ == '__main__':
    main()
