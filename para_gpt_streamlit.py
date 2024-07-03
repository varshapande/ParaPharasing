import streamlit as st
import os
import json
from openai import OpenAI

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = ''

# Initialize OpenAI client
client = OpenAI()

def generate_paraphrase(user_prompt, sys_prompt):
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = client.ChatCompletion.create(
        model="gpt-4-turbo",
        n= 4,
        messages=messages
    )

    paraphrased_text = response['choices'][0]['message']['content']
    return paraphrased_text

def main():
    st.title("Text Paraphraser with OpenAI GPT-4 Turbo")

    # Input text field for user prompt
    user_prompt = st.text_area("Enter text to paraphrase:")

    if st.button("Paraphrase"):
        if user_prompt:
            sys_prompt = """
            You are an AI model that can paraphrase text inputs given by the user.
            and please make ensure generate four different responses
            Give the output in the following JSON format:
            
            {"paraphrased_text_1": [write paraphrased text here]
               "paraphrased_text_2": [write paraphrased text here
                "paraphrased_text_3": [write paraphrased text here
                "paraphrased_text_4": [write paraphrased text here
               
               }
            """
            paraphrased_text = generate_paraphrase(user_prompt, sys_prompt)
            st.write(f"Original Text: {user_prompt}")
            st.write(f"Paraphrased Text: {paraphrased_text}")

if __name__ == "__main__":
    main()
