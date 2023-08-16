import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64

st.set_page_config(page_title="Voting Page", page_icon="📈")

st.markdown("# Voting Page")

st.write('您同意PitNETs 納入重大傷病嗎')

# Try to Load existing data
try:
    dat = pd.read_csv('survey_results.csv')

except FileNotFoundError:
    dat = pd.DataFrame(columns=['Q1', 'Specialty'])

# Options for answers
Q1 = st.selectbox(
    ' ',
    ('Yes', 'No')
)

# Second question
st.write('What is your specialty?')
specialty = st.selectbox(
    '  ',
    ('Endocrine', 'Surgeon', 'Pathologist', 'Others')
)

if st.button('Submit', key='submit_button2'):
    # Append the new response
    dat = dat.append({
        'Q1': Q1,
        'Specialty': specialty
    }, ignore_index=True)

    # Save the updated data
    dat.to_csv('survey_results.csv', index=False)
    
    st.success('Your response has been recorded.')


    

Preference, Specialty = st.columns(2)

# Plot the survey results
with Preference:
    st.write('### Preference')
    fig1, ax1 = plt.subplots()
    dat['Q1'].value_counts().plot(kind='bar', ax=ax1)
    ax1.set_xlabel('Response')
    ax1.set_ylabel('Count')
    st.pyplot(fig1)

# Plot for second question
with Specialty:
    st.write('### Specialty')
    fig2, ax2 = plt.subplots()
    dat['Specialty'].value_counts().plot(kind='bar', ax=ax2)
    ax2.set_xlabel('Specialty')
    ax2.set_ylabel('Count')
    st.pyplot(fig2)


if st.button('Download', key='download_button'):
    csv = dat.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="survey_results.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)