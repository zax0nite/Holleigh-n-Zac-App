import streamlit as st
import json
import random
from PIL import Image
import os

# Load messages from JSON
with open("formatted_messages.json", "r", encoding="utf-8") as file:
    messages = json.load(file)["messages"]

# Load images from the "Images" folder
image_folder = "Images"
images = [
    os.path.join(image_folder, img) 
    for img in os.listdir(image_folder) 
    if img.lower().endswith((".png", ".jpg", ".jpeg"))
]


# Function to filter messages by author
def get_messages(author):
    return [msg for msg in messages if msg["author"] == author]

# Initialize session state for message and image
if "current_message" not in st.session_state:
    st.session_state["current_message"] = None

if "current_image" not in st.session_state:
    st.session_state["current_image"] = None

# Streamlit App Layout
st.set_page_config(page_title="Holleigh & Zac's Special App", page_icon="💖")
st.title("Holleigh & Zac's Special App 💕")

# Toggle for who is using the app
author = st.radio("Who is using the app?", ["Holleigh", "Zac"])

# Button to display a new random message
if st.button("Show New Message"):
    # Show messages FROM Zac if Holleigh is using the app, and vice versa
    recipient = "Holleigh" if author == "Zac" else "Zac"
    filtered_messages = get_messages(recipient)
    if filtered_messages:
        st.session_state["current_message"] = random.choice(filtered_messages)

# Button to display a new random image
if st.button("Show Random Image"):
    if images:
        st.session_state["current_image"] = random.choice(images)

# Display the current message
if st.session_state["current_message"]:
    message = st.session_state["current_message"]
    st.write(f"**{message['text']}**")
    st.write(f"_Sent on: {message['date']}_")

# Display the current image
if st.session_state["current_image"]:
    img = Image.open(st.session_state["current_image"])
    st.image(img, use_container_width=True)  # Updated to use `use_container_width`

# Footer
st.write("---")
st.caption("Made with ❤️ by Zac")
