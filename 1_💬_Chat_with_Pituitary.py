import streamlit as st

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt


# Your API endpoint
API_URL = "https://endo.onrender.com/api/v1/prediction/c2732f4d-c665-4988-9665-ccee123843b7"

def query_api(question):
    payload = {"question": question}
    response = requests.post(API_URL, json=payload)
    return response.json()

# Streamlit app layout

import streamlit as st

#st.set_page_config(page_title="Plotting Demo", page_icon="📈")
st.set_page_config(page_title="💬 Chat with Pituitary gland", page_icon="💬",layout="wide")
st.title("💬 Chat with Pituitary gland ")


user_input = st.text_input("***If you encounter any error, just hit submit again***", "腦垂體腫瘤的新分類？  ")

response = None

# ... (other parts of your script)

# Check if 'response' is not None before trying to access its 'text' attribute
if response is not None:
    st.markdown(response['text'])
else:
    st.markdown("No response received.")

if st.button("Submit", key='submit_button1'):
        response = query_api(user_input)
    #st.write(response)  # Display the API response
        

answer_col, sources_col = st.columns(2)
        
with answer_col:
        st.markdown("#### Answer")
        st.markdown(response['text'])

with sources_col:
        st.markdown("#### Top 1 match from file")
        for source in response['sourceDocuments']:
                st.markdown(source['pageContent'])
                st.markdown("Data from:" + str(source['metadata']['name']))
                st.markdown("---")
                
st.sidebar.success("Please visit Voting Page if you finish chating with pituitary gland.")

with st.sidebar:
      #  st.markdown("")
        st.markdown("# About 💬")
        st.markdown(
                "The question is answered by a large language model \n, so apology first if the answer is not smart enough.")
        
        st.markdown(
                "Reference from Overview of the 2022 WHO Classification of Pituitary Tumors")
        
        
       # st.markdown(
       #         "Please visit voting page if finishing chat with pituitary gland")
        #st.markdown(
        #        "腦垂體專刊 \n"
        #)
        st.markdown("    ")
        st.markdown("Contact me if any technical problem \n"
                    "brightlight@vghtc.gov.tw  李宇璇")
    #st.markdown("Kept online by [Ben's Bites](%s)!" %bb_url)

                

                
                

        
