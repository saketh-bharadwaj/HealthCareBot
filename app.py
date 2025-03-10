import streamlit as st
from transformers import pipeline

# Load the chatbot model
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare(userInput):
    # Custom responses for specific keywords
    if "symptom" in userInput.lower():
        return "Please consult a doctor for symptoms."
    elif "appointment" in userInput.lower():
        return "Please book an appointment with a healthcare provider."
    elif "medication" in userInput.lower():
        return "Please consult a doctor for medication guidance."
    else:
        # Generate a response using the chatbot model
        response = chatbot(userInput, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    # Streamlit app title
    st.title("Healthcare Assistant Chatbot")
    
    # Input box for user query
    userInput = st.text_input("How can I assist you today?")
    
    # Button to submit the query
    if st.button("Submit"):
        if userInput:
            st.write("**User:**", userInput)
            response = healthcare(userInput)
            st.write("**Healthcare Assistant:**", response)
        else:
            st.write("Please enter a message.")

# Run the main function
main()
