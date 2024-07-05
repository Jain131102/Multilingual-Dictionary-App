import requests
import streamlit as st
from languages import *

url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"


class State:
    """This is the app state."""

    text = ""
    language = ""
    define = ""

    @staticmethod
    def get_meaning():
        """Get the meaning of the entered text in the specified language."""

        # Check if text is entered
        if not State.text:
            st.warning("Please enter some text.")
            return

        # Check if a language is selected
        if not State.language:
            st.warning("Please select a language.")
            return

        # Generate prompt for OpenAI API
        prompt = f"get meaning of '{State.text}' in {State.language}"

        try:
            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "system_prompt": "",
                "temperature": 0.9,
                "top_k": 5,
                "top_p": 0.9,
                "max_tokens": 256,
                "web_access": False
            }
            headers = {
                "x-rapidapi-key": "use your api key from rapid api site",
                "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
                "Content-Type": "application/json",
                "X-RapidAPI-Mock-Response": "200"
            }
            response=requests.post(url, json=payload, headers=headers)
            State.define = response.json()["result"]

        except Exception as e:
            # Handle errors from OpenAI API
            st.error(f"Error with OpenAI API: {e}")

    @staticmethod
    def set_text(text):
        """Set the entered text in the app state."""
        State.text = text

    @staticmethod
    def set_language(language):
        """Set the selected language in the app state."""
        State.language = language


def main():
    # Set Streamlit page configuration
    st.set_page_config(
        page_title="Streamlit: Multilingual Dictionary App",
        page_icon=":globe_with_meridians:",
        layout="wide",
    )

    # Main title of the app
    st.title("Multilingual Dictionary App")

    # Text area for user input
    State.text = st.text_area("Enter text")

    # Dropdown for selecting a language
    State.language = st.selectbox("Select a language", languages)

    # Button to trigger the meaning retrieval
    if st.button("Get Meaning", key="meaning_button"):
        State.get_meaning()

    # Horizontal line for visual separation
    st.markdown("---")

    # Display the retrieved definition
    if State.define:
        st.subheader("Definition:")
        st.write(State.define)


# Run the app when the script is executed
if __name__ == "__main__":
    main()


# response = requests.post(url, json=payload, headers=headers)

# print(response.json())
