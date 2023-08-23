import streamlit as st

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

def query_api(question):
    payload = {"question": question}
    response = requests.post(API_URL, json=payload)    
    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON response.")
            print("Response content:", response.text)
            #return None
    else:
        print("Received error response:", response.status_code, response.text)
        #return None


#st.set_page_config(page_title="Plotting Demo", page_icon="📈")
st.set_page_config(page_title="💬 Chat with Pituitary gland", page_icon="💬",layout="wide")
st.title("💬 Chat with Pituitary gland ")


#st.sidebar.success(" Please visit Voting Page if you finish chating with pituitary gland.")

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

                


# Your API endpoint
API_URL = "https://endo.onrender.com/api/v1/prediction/c2732f4d-c665-4988-9665-ccee123843b7"


user_input = st.text_input("***You can ask anything about 2022 WHO classification of pituitary tumors, if you encounter any error, just hit submit again***", "為什麼要將pituitary adenoma 改名為Pituitary neuroendocrine tumors?")

response = None  # Initialize response to None

if st.button("Submit", key='submit_button1'):
    if user_input:
        response = query_api(user_input)
        if response is None:
            st.write("Failed to get a valid response from the ChatGPT API.")
    else:
        st.write("Please enter a valid question.")       

answer_col, sources_col = st.columns(2)

if response:  # Check if response is not None
    with answer_col:
        st.markdown("#### Answer")
        st.markdown(response['text'])

    with sources_col:
        st.markdown("#### Top 1 match from file")
        for source in response['sourceDocuments']:
            st.markdown(source['pageContent'])
            st.markdown("Data from:" + str(source['metadata']['name']))
            st.markdown("---")


st.write("**Please visit Voting Page if you finish chating with pituitary gland.**")
                

                
                

        
