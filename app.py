import streamlit as st
import joblib
from obj import PreProcessText
import sklearn
import pandas as pd

obj = PreProcessText()
train_file_path = "train-data.tsv"
df_train=pd.read_csv(train_file_path,sep='\t',header=None)
bow_transformer = sklearn.feature_extraction.text.CountVectorizer(analyzer=obj.token_words).fit(df_train[1])

model=joblib.load("sms_model")

st.title("Spam-Ham Detection")

input_message=st.text_input(label="text")

def prediction(input_message):
    messages_bow = bow_transformer.transform([input_message])
    tfidf_transformer = sklearn.feature_extraction.text.TfidfTransformer().fit(messages_bow)
    messages_tfidf = tfidf_transformer.transform(messages_bow)

    prediction = model.predict(messages_tfidf)
    st.write(prediction)

st.button('Predict',on_click=lambda: prediction(input_message))
