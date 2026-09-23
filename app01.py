import streamlit as st
import ollama

# Page Configuration
st.set_page_config(page_title="CHATBAT", page_icon="🦇")

st.title("🦇 CHATBAT AI MODEL")
st.markdown("ask anything, cook something😋")

# Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for Model Selection
with st.sidebar:
    st.header("Settings")
    try:
        # Fetch available models from Ollama
        models_info = ollama.list()
        # The structure of list() response can vary by version,
        # usually it's a list of model objects with a 'name' attribute.
        model_names = [m.model for m in models_info.models]
    except Exception as e:
        st.error(f"Could not connect to Ollama: {e}")
        model_names = []

    if model_names:
        selected_model = st.selectbox("Choose a model", model_names)
    else:
        st.warning("No models found. Please run 'ollama pull llama3' in your terminal.")
        selected_model = None

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask me anything..."):
    if not selected_model:
        st.error("Please select a model from the sidebar first!")
    else:
        # Add user message to state
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate AI response
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            try:
                # Stream response from Ollama
                stream = ollama.chat(
                    model=selected_model,
                    messages=st.session_state.messages,
                    stream=True,
                )

                for chunk in stream:
                    content = chunk.message.content
                    full_response += content
                    response_placeholder.markdown(full_response + "▌")

                response_placeholder.markdown(full_response)

                # Add assistant message to state
                st.session_state.messages.append({"role": "assistant", "content": full_response})

            except Exception as e:
                st.error(f"An error occurred: {e}")
