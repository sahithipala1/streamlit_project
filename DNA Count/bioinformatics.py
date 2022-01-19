import streamlit as st
import pandas as pd
import altair as alt
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

sequence_input = ">DNA Query 2\nGATGTAGTGTAGAAAAAGGGATGTGTGCACTCGCAC" \
                 "\nTCCCCCGAGTGACCCCCCCCGAGCCCCCCCCAGAGTGATGATGAGATGATGT "

sequence = st.text_area(" Sequence input :", sequence_input, height=250)

sequence = sequence.splitlines()

sequence = sequence[1:]

sequence = "".join(sequence)

st.write("""

***
""")

st.header("INPUT (DNA Query)")
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader("1.Print Dictionary")


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d


X = DNA_nucleotide_count(sequence)

# X_label = list(X)
# X_value = list(X.values()
X


# 2. Print Text
st.subheader('2. Print Text')
st.write("There are  " + str(X['A']) + " adenine (A)")
st.write(" There are  " + str(X['T']) + " thymine (T) ")
st.write(" There are  " + str(X['G']) + "adenine (G) ")
st.write(" There are  " + str(X['C']) + " thymine (C) ")

# 3.Display Data Frame
st.subheader('3.Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

# 4.Display bar chart using ALTAir
st.subheader('4.Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(x='nucleotide', y='count')
p = p.properties(width=alt.Step(90))
st.write(p)
