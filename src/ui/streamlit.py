import json
import requests
import streamlit as st

# Assigning title to UI
st.title("LLM HTML Parser 🔍")

# Description about the app
st.write("An HTML Parsing app powered by LLM.")

# Taking HTML Content from user
html_code = st.text_area("Enter HTML Code Snippet", height=200) 

# HTML Parsing
if st.button("Parse HTML"):
    if html_code:
        # Sending HTML block to FastAPI endpoint
        url="http://127.0.0.1:8000/parse_html/?html_input="

        res = requests.post(url, 
                            json={"content": html_code})
        
        print(type(res))
        
        if res.status_code == 200:
            st.subheader(f"Response from LLM :")
            st.json(res.json())
        else:
            st.error(f"Error: {res.status_code} - {res.text}")

    else:
        st.warning("Please enter some HTML code")