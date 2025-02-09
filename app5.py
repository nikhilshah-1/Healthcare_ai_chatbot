import streamlit as st
from transformers import pipeline
import re

# Load the chatbot model
chatbot = pipeline("text-generation", model="openai-community/gpt2")

# Define the healthcare chatbot
def healthCare_chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    # Rule-based responses with regular expressions
    if re.search(r"\bsymptom\b", user_input):
        return "Please consult a doctor for more accurate advice."
    elif re.search(r"\bappointment\b", user_input):
        return "Would you like to schedule an appointment with a doctor?"
    elif re.search(r"\bmedication\b", user_input):
        return "It is important to consume prescribed medicines regularly. If you have concerns, consult your doctor."
    elif re.search(r"\bemergency\b", user_input):
        return "If this is a medical emergency, please call your local emergency number immediately."
    else:
        # Generate a response using the text-generation model
        try:
            response = chatbot(user_input, max_length=500, num_return_sequences=1)
            if response and len(response) > 0:
                generated_text = response[0]['generated_text']
                # Ensure response stops at a full stop
                sentences = generated_text.split('.')
                generated_text = '. '.join(sentences[:10]) + '.'  
                if "sorry" in generated_text.lower() or "don't know" in generated_text.lower():
                    return "I'm sorry, I couldn't generate a relevant response. Please try rephrasing your question."
                return generated_text
            else:
                return "I'm sorry, I couldn't generate a response. Please try rephrasing your question."
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

# Main Streamlit app
def main():
    st.set_page_config(page_title="HealthCare Assistant ChatBot", page_icon="🏥")

    st.title("HealthCare Assistant ChatBot")
    st.write("Welcome! How can I assist you today?")
    
      # Sidebar for additional information
    with st.sidebar:
        st.markdown("### About")
        st.write("This is a healthcare assistant chatbot designed to help you with general medical queries.")
        st.write("**Disclaimer:** This chatbot is not a substitute for professional medical advice. Always consult a doctor for serious concerns.")
        st.markdown("---")
        st.markdown("### Suggested Queries")
        st.write("Try these examples:")
        st.write("- What are the symptoms of [disease]?")
        st.write("- How can I boost my immunity?")
        st.write("- How much water should I drink daily?")
        st.markdown("---")
    

    # Suggested Queries (Displayed in a Horizontal Row)
    st.markdown("### **Suggested Queries**")

    suggested_queries = [
        "What are the symptoms of flu?",
        "What to do in case of a heart attack?",
        "How can I boost my immunity?",
        "How much water should I drink daily?"
    ]

    cols = st.columns(len(suggested_queries))  # Create horizontal columns

    for i, query in enumerate(suggested_queries):
        with cols[i]:  # Place buttons inside each column
            if st.button(query):
                st.session_state.user_input = query
                st.session_state.submit = True  

    st.markdown("---")
     # Input field for user query with an Enter button
    user_input = st.text_input("Enter your query:", key="user_input", on_change=lambda: st.session_state.update(submit=True))
    submit_button = st.button("Submit")

    # Auto-process if a suggested query was clicked
    if (user_input and len(user_input.strip()) > 3) and (submit_button or st.session_state.submit):
        with st.spinner("Processing your query. Please wait..."):
            response = healthCare_chatbot(user_input)
            st.write(f"**Healthcare Assistant:** {response}")
        st.session_state.submit = False  # Reset after processing

if __name__ == "__main__":
    main()
