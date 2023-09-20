import streamlit as st
from company_email_sent import send_company_email

with st.form(key='company_contact_form'):
    email_address = st.text_input("Enter your email")
    selection_box = st.selectbox('What topic to you want to discuss', ['Job Inquiries', 'Project Proposal', 'Other'], key='select_box')
    raw_message = st.text_input("Enter your message here")
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        print("Form submitted")
        message = f"""\
Subject: {selection_box}
        
From: Message from {email_address}

{raw_message}
        """
        st.write(message)
        send_company_email(message)
        print('Message sent for real:  SUCCESS!!!!!')

   #     st.experimental_rerun()

