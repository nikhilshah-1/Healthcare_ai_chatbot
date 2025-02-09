
# AI-Powered Health Assistant

## Overview
The **AI-Powered Health Assistant** is a chatbot designed to assist users with general healthcare-related queries. It utilizes a combination of **rule-based responses and AI-generated text (GPT-2)** to provide accurate and dynamic responses.

## Features
✅ Rule-based responses for common health-related queries  
✅ AI-generated responses using **GPT-2** when rule-based answers are not available  
✅ **Streamlit-based UI** for an intuitive user experience  
✅ **Suggested Queries** that auto-fill and generate responses when clicked  
✅ **Regular Expressions** for keyword matching and response filtering  
✅ **Easy Deployment** with Python and Streamlit  

## Technology Stack
- **Programming Language:** Python
- **Framework:** Streamlit
- **AI Model:** GPT-2 (via Hugging Face Transformers)
- **Libraries:** Transformers, Regex, Streamlit

## Installation
To run the chatbot locally, follow these steps:

### Prerequisites
Ensure you have Python installed (version 3.7+ recommended). Install dependencies using:
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
streamlit run app.py
```
This will launch the chatbot interface in your browser.

## Project Structure
```
├── app.py               # Main chatbot application
├── requirements.txt     # List of dependencies
├── README.md           # Project documentation
├── assets/             # Images and supporting files
```

## Usage
1. Open the chatbot UI.
2. Enter a healthcare-related question.
3. Select a **Suggested Query** for instant responses.
4. Receive AI-generated or rule-based answers.

## Future Improvements
🚀 Integration with a **medical knowledge base** for enhanced accuracy  
🚀 Support for **multiple languages**  
🚀 Addition of **voice-based interaction**  

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

