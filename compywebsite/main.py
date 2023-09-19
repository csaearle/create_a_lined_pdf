import streamlit as st
import pandas

st.set_page_config(layout="wide")


content_1 = "The best company"
content_2 = """   Lorem ipsum dolor Lorem ipsum dolor sit amet. Non obcaecati placeat in omnis maxime
 nam ipsum dicta ex sint reiciendis hic dolor commodi quo fugit nisi. Nam rerum autem ut eaque quos et
  ipsam corrupti est quod fugiat. Qui quae modi eum eligendi perferendis nam reprehenderit rerum.

Est dignissimos autem aut nihil tempora id fugiat saepe eos rerum nesciunt ut ratione tenetur et
 dolor quas sed blanditiis amet. Qui maxime optio aut perspiciatis suscipit aut sint omnis. Eum
  voluptas nemo At provident consectetur et quod omnis et dolores dolores. Est dolore nesciunt 
  
"""


st.title(content_1)
st.write("")
st.write(content_2)
st.write("")



col_sep, col1, col_space1, col2, col_space2, col3, col_end = st.columns([1, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")


with col1:
    st.subheader("Our Team")
    st.write("")
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image("../images/" + row["image"])
        st.write("")
        st.write(" ")
        st.write(" ")

with col2:
    st.write("")
    st.write("")
    st.write(" ")
    st.write(" ")

    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("../images/" + row["image"])
        st.write("")
        st.write(" ")
        st.write(" ")


with col3:
    st.write("")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("../images/" + row["image"])
        st.write("")
        st.write(" ")
        st.write(" ")





