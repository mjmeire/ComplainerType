import streamlit as st
import transformers 

from transformers import pipeline
classifier = pipeline(model="matmei/complainerType")

# Define your function f() here
def f(text):
    return classifier(text)

def main():
    # Set page title
    st.title("Complainer classification App")

    # Get user input text
    user_input = st.text_input("Enter the complaint you want to analyze:")

    # Apply function f() when Submit button is clicked
    if st.button("Submit"):
        result = f(user_input)
        st.success("Classification: {}".format(result))

if __name__ == "__main__":
    main()