import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationTokenBufferMemory
from langchain.llms import LlamaCpp

from utils.prompts import nice_guy_prompt_token_template

# Set Streamlit page configuration
st.set_page_config(page_title="🧠MemoryBot🤖", layout="wide")
# Initialize session states
if "saved_chats" not in st.session_state:
    st.session_state["saved_chats"] = []
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Define function to get user input
def get_text():
    """
    Get the user input text.

    Returns:
        (str): The text entered by the user
    """
    input_text = st.text_input(
        "You: ",
        st.session_state["input"],
        key="input",
        placeholder="Your AI assistant here! Ask me anything ...",
        label_visibility="hidden",
    )
    return input_text


# Define function to start a new chat
def new_chat():
    """
    Clears session state and starts a new chat.
    """
    st.session_state["saved_chats"].append(st.session_state.messages)
    st.session_state.messages = []
    st.session_state.entity_memory.clear()


# Set up the Streamlit app layout
st.title("🤖 Llama 2 Chat Bot with Memory🧠")
st.subheader(" Powered by 🦜 LangChain + Meta + Streamlit")


# Create an OpenAI instance
llm = LlamaCpp(
    temperature=0.9,
    model_path=st.secrets.LLAMA_PATH,
    max_tokens=1024,
    n_ctx=4128,
)

# Create a ConversationEntityMemory object if not already created
if "entity_memory" not in st.session_state:
    st.session_state.entity_memory = ConversationTokenBufferMemory(
        llm=llm,
        max_token_limit=2048,
        human_prefix="",
        ai_prefix="",
    )

# Create the ConversationChain object with the specified configuration
Conversation = ConversationChain(
    llm=llm,
    prompt=nice_guy_prompt_token_template,
    memory=st.session_state.entity_memory,
)

# Add a button to start a new chat
st.sidebar.button("New Chat", on_click=new_chat, type="primary")


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    prompt = prompt.strip().replace("  ", " ")
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Generating answer..."):
        output = Conversation.run(input="[INST] " + prompt + " [/INST]\n")
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": output})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(output)

# Display stored conversation sessions in the sidebar
for i, sublist in enumerate(st.session_state.saved_chats):
    with st.sidebar.expander(label=f"Conversation {i}"):
        st.write(sublist)

# Allow the user to clear all stored conversation sessions
if st.session_state.saved_chats:
    if st.sidebar.button("Clear-all"):
        del st.session_state.saved_chats
