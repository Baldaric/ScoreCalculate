import streamlit as st
import pandas as pd
import phase0
import phase1

st.set_page_config(page_title="Score Calculate", layout="wide")

with st.sidebar:
    st.image('ratna.png')
    st.title('About')
    st.write('Just to calculate your score')
    st.write('______')

    st.title('Navigation Pane')
    navigation = st.selectbox('Go To Page', ['Phase 0','Phase 1'])



if navigation == 'Phase 0':
    phase0.run()
elif navigation == 'Phase 1':
    phase1.run()