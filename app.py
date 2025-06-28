import streamlit as st
import requests

st.set_page_config(
    page_title="CAT - CleanData Automation Tool",
    page_icon="🐱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        .cat-box {
            background-color: #FFF8DC;
            padding: 40px 50px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            max-width: 900px;
            margin: auto;
            margin-top: 30px;
        }
        .cat-box h2 {
            text-align: center;
            color: #333333;
        }
        .cat-box p {
            text-align: center;
            color: #444444;
            font-size: 15px;
            line-height: 1.6;
        }
        .cat-box h4 {
            text-align: center;
            margin-top: 30px;
            color: #333333;
        }
    </style>

    <div class="cat-box">
        <h2>CAT : CleanData Automation Tool</h2>
        <p>
            Get ready to clean your data effortlessly remove empty rows and columns, trim whitespaces, standardize column names, correct data types, handle missing values, eliminate duplicates, fix inconsistent categories, tidy up text, auto-tag descriptions using AI, log every transformation, and export a polished Excel or CSV file all with just one click.
        </p>
        <h4>Upload your Excel or CSV file</h4>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    uploaded_file = st.file_uploader(
        "Upload your Excel or CSV file",
        type=["xlsx", "csv"],
        label_visibility="collapsed"
    )

    if uploaded_file is not None:
        st.success(f"✅ `{uploaded_file.name}` uploaded! Sending to HATI for cleaning...")

        # Determine content type
        content_type = (
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            if uploaded_file.name.endswith(".xlsx")
            else "text/csv"
        )


        files = {
            'file': (
                uploaded_file.name,
                uploaded_file,
                content_type
            )
        }


        try:
            response = requests.post("https://areebahmad22.app.n8n.cloud/webhook-test/cat/clean", files=files)
            if response.ok:
                st.success("File cleaned successfully!")
                st.download_button(
                    label="Download Cleaned File",
                    data=response.content,
                    file_name="Cleaned_Output.xlsx"
                )
            else:
                st.error("Something went wrong while processing the file.")
        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to the backend.\n\n{e}")
