import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
menu = ["Home", "About", "Contact"]
choice = st.sidebar.radio("Go to", menu)

# Display content based on menu selection
if choice == "Home":
    st.title("Home Page")
    st.write("Welcome to the Home page!")
elif choice == "About":
    st.title("About Page")
    st.write("This is the About page.")
elif choice == "Contact":
    st.title("Contact Page")
    st.write("Contact us here.")
