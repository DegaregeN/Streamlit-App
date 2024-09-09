import streamlit as st

# --- PAGE SETUP ---
def about_page():
    st.title("About Me")
    st.write("This is About Me page.")

def project_1_page():
    st.title("Telecom Dashboard")
    st.write("This is the Telecom Dashboard page.")

def project_2_page():
    st.title("Chat Bot")
    st.write("This is the Chat Bot page.")

# --- NAVIGATION SETUP ---
pages = {
    "About Me": about_page,
    "Telecom Dashboard": project_1_page,
    "Chat Bot": project_2_page,
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# --- RUN SELECTED PAGE ---
page = pages[selection]
page()
