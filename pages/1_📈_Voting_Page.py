import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64

plt.rcParams['font.family'] = 'WenQuanYi Zen Hei'

st.set_page_config(page_title="Voting Page", page_icon="📈")

st.markdown("# Voting Page")

st.write('在WHO 將PitNETs 定義為惡性後,您會將新診斷PitNETs 的病人申請重大傷病嗎')

# Try to Load existing data
try:
    dat = pd.read_csv('survey_results.csv')

except FileNotFoundError:
    dat = pd.DataFrame(columns=['Q1', 'Specialty'])

# Options for answers

# Options for answers
Q1 = st.selectbox(
    ' ',
    ('Yes', 'No', 'Sometimes')
)

# If user selects '某些情況會', prompt them for a reason
reason = ""
if Q1 == 'sometimes':
    reason = st.text_input("什麼時候會想幫病人申請重大傷病:")

# Second question
st.write('What is your specialty?')
specialty = st.selectbox(
    '  ',
    ('Endocrine', 'Surgeon', 'Pathologist', 'Others')
)

if st.button('Submit', key='submit_button2'):
    new_row = pd.DataFrame({
    'Q1': [Q1],
    'Reason': [reason],  # adding the reason to the dataframe
    'Specialty': [specialty]})
    dat = pd.concat([dat, new_row], ignore_index=True)

    # Save the updated data
    dat.to_csv('survey_results.csv', index=False, encoding='utf-8-sig')

    st.success('Your response has been recorded.')    

Preference, Specialty = st.columns(2)

font_properties = {'family':'WenQuanYi Zen Hei', 'size': 14}


# Plot the survey results
with Preference:
    st.write('## Preference')
    fig1, ax1 = plt.subplots()
    dat['Q1'].value_counts().plot(kind='bar', ax=ax1)
    ax1.set_xlabel('Response',fontdict=font_properties)
    ax1.set_ylabel('Count',fontdict=font_properties)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0, fontdict=font_properties)
    ax1.tick_params(axis='both', which='major', labelsize=14)
    st.pyplot(fig1)

# Plot for second question
with Specialty:
    st.write('## Specialty')
    fig2, ax2 = plt.subplots()
    dat['Specialty'].value_counts().plot(kind='bar', ax=ax2)
    ax2.set_xlabel('Specialty',fontdict=font_properties)
    ax2.set_ylabel('Count',fontdict=font_properties)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0, fontdict=font_properties)
    ax2.tick_params(axis='both', which='major', labelsize=14)
    st.pyplot(fig2)


if st.button('Download', key='download_button'):
    csv = dat.to_csv(index=False, encoding='utf-8-sig')
    dat.head(3)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="survey_results.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
