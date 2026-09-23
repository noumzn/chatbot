
# Ollama Local Chatbot with Streamlit

This is a simple, private chatbot interface that runs entirely on your local machine.

## Prerequisites

1. **Install Ollama**: Download and install Ollama from [ollama.com](https://ollama.com/).
2. **Pull a Model**: After installing Ollama, open your terminal and download a model (e.g., Llama 3):
   ```bash
   ollama pull llama3
   ```

## Setup

1. **Clone this repository** (or navigate to the project folder).
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the Streamlit app by running:
```bash
streamlit run app.py
```

## How it Works
- **Frontend**: Built with Streamlit for a reactive, web-based UI.
- **Backend**: Communicates with the Ollama local API via the `ollama-python` library.
- **Privacy**: Your data never leaves your machine.

# chatbot
An AI-powered chatbot built with Streamlit and Ollama, featuring a modern conversational interface and local AI capabilities.

