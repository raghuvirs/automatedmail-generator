import streamlit as st
from orchestrator import run_mail_pipeline

st.set_page_config(page_title="Automated AI Mail Generator", page_icon="✉️")

st.title("📧 Automated AI Mail Generator")

with st.form("email_form"):
    subject = st.text_input("Subject")
    recipient = st.text_input("Recipient Email")
    message = st.text_area("Message")
    sender = st.text_input("Your Email Address (Sender)")
    tone = st.selectbox(
                "Select Email Tone",
                ("Formal", "Informal", "Casual", "Appreciative", "Apologetic")
            )
    attachments = st.file_uploader("Upload Attachment(s)", accept_multiple_files=True)



    submitted = st.form_submit_button("Send Email")

    if submitted:
        with st.spinner("Generating and sending your email..."):
           result = run_mail_pipeline(subject, recipient, message, sender, tone, attachments)
        st.success(result)
