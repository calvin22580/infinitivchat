import streamlit as st
import requests
import json

# Set the API endpoint and token.
API_ENDPOINT = "https://<your-api-endpoint>"
AUTH_TOKEN = "Bearer <your-auth-token>"

headers = {"Authorization": AUTH_TOKEN, "Content-Type": "application/json"}

def send_post_request(question):
    data = {"question": question}
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json() # Assuming the response data is in JSON format
    else:
        st.write(f"Request failed with status code {response.status_code}")

st.title("Chatbot")

user_input = st.text_input("Ask a question")

if st.button("Send"):
    response = send_post_request(user_input)
    if response:
        st.write(response)