import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings

warnings.filterwarnings("ignore")
model = pickle.load(open("Model_Sales.pkl","rb")) #loading the created model


st.set_page_config(page_title="Future Sales Prediction Application") #tab title

#prediction function
def predict_status(TV, Radio, Newspaper):
    input_data = np.asarray([TV, Radio, Newspaper])
    input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)
    return prediction[0]

def main():

    # titling your page
    st.title("Future Sales Prediction Application")

    #getting the input
    TV = st.text_input("Enter your TV Budget(dollars)")
    Radio = st.text_input("Enter your Radio Budget(dollars)")
    Newspaper = st.text_input("Enter your Newspaper(dollars)")

    #predict value
    diagnosis = ""

    if st.button("Predict"):
    
        diagnosis = predict_status(TV, Radio, Newspaper)
        st.info(f"You're Sale is: {} Units", diagnosis)

    st.write(" ")    
    st.write("Project by Akshay Narvate")
    
            
if __name__=="__main__":
    main()
