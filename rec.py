# Author: Kwa Chin Soon
# version: 2.0
# Nov 2022

import streamlit as st
# other libs
import pandas as pd


# -- Set page config
apptitle = 'Justin-Time Periodic Inspection'

st.set_page_config(page_title=apptitle, page_icon='random', layout= 'wide')
# random icons in the browser tab

st.title('Justin-Time Periodic Inspection')


 ######################## section-1 ##################
 # Let's add a sub-title
st.write("Identifying similar at-risk buildings")

df1 = pd.read_csv('rec.csv') 

T7 = st.text_input("Enter Postal Code of Building that has been labelled T7:", "")

if st.button("Show Address"):
    st.write('The building address is at 153 TYRWHITT ROAD QINAN BUILDING SINGAPORE 207566.')

if st.button("Display 30 similar buildings"):
        st.dataframe(df1)

