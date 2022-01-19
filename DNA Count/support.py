import altair as alt
import streamlit as st
from PIL import Image

image = Image.open("dna.jpg")

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide count web App

This app counts the nucleotide of query DNA!

***
""")

############################
# Input Text Box
###########################

st.header("Enter DNA sequence")
