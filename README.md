# Multilingual Dictionary App
The `Multilingual Dictionary App` is designed to help users obtain definitions of words or phrases in different languages using OpenAI's language models. The app features a simple user interface where users can input text and select a language from a dropdown menu , built with Streamlit.

## Features

- **Text Input**: Users can `enter any text` they wish `to define`.
- **Language Selection**: A dropdown menu allows users to choose from a `variety of languages`.
- **Meaning Retrieval**: Upon clicking the `Get Meaning` button, the app fetches the meaning of the entered text in the selected language.
- **Error Handling**: The app provides warnings if no text or language is selected.

## Requirements

To run this application, you need the following:

- Python 3.x
- Streamlit
- Requests library
- OpenAI API key (from RapidAPI)

## Installation

1. **Install Required Libraries**:
   ```bash
    pip install -r requirements.txt
   ```

2. **Get OpenAI API Key**:
- Sign up at [RapidAPI](https://rapidapi.com/) and subscribe to the ChatGPT API.
- Obtain your API key.

3. **Set Environment Variables** (optional):
- You can set your API key as an environment variable for security:
  ```bash
  export RAPIDAPI_KEY='your_api_key'
  ```

## Usage

1. Save the provided code into a file named `app.py`.
2. Run the application:
   ```bash
   streamlit run app.py
   ```
3. Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## Code Structure

### `app.py`

This is the main application file that contains:

- **State Class**: Manages the state of user input and selected language.
- **get_meaning() Method**: Sends a request to the OpenAI API to get the meaning of the entered text.
- **set_text() and set_language() Methods**: Update the state with user inputs.
- **main() Function**: Configures Streamlit settings and handles user interactions.

### `languages.py`

This file contains a list of supported languages for definition retrieval.


## Example Usage

1. Enter a word or phrase in the text area.
2. Select a language from the dropdown list.
3. Click on "Get Meaning" to retrieve the definition.

## Troubleshooting

- Ensure that your API key is correct and has not expired.
- Check your internet connection if you encounter issues with API requests.

## Conclusion

The Multilingual Dictionary App is a powerful tool for language learners and anyone interested in understanding words in various languages. By leveraging OpenAI's capabilities, it provides quick and accurate definitions, enhancing communication across language barriers.


## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

