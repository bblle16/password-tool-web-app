import streamlit as st
import re
import random
import string
import pyperclip  # Clipboard handling

# 🔐 Password Strength Checker
def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    feedback = []
    if length_error:
        feedback.append("Password should be at least 8 characters.")
    if digit_error:
        feedback.append("Add at least one number.")
    if uppercase_error:
        feedback.append("Include an uppercase letter.")
    if lowercase_error:
        feedback.append("Include a lowercase letter.")
    if symbol_error:
        feedback.append("Use a special character (!@#$%^&* etc).")

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score in [3, 4]:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, color, feedback

# 🔑 Password Generator
def generate_password(length=12):
    if length < 8:
        return "Password too short!", False

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password, True

# 🌐 Streamlit Web UI
st.set_page_config(page_title="Password Tool", page_icon="🔐")

# Dark Mode Toggle
if st.checkbox("Enable Dark Mode"):
    st.markdown(
        """
        <style>
        body {
            background-color: #1e1e1e;
            color: white;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

st.title("🔐 Password Strength Checker & Generator")

# -- Checker Section
st.header("🔒 Check Your Password Strength")
user_password = st.text_input("Enter your password", type="password", key="user_pass")

if st.button("Check Strength"):
    if not user_password:
        st.warning("Please enter a password.")
    else:
        strength, color, feedback = check_password_strength(user_password)
        st.markdown(f"**Password Strength:** :{color}[{strength}]")
        if feedback:
            st.markdown("**Suggestions to improve:**")
            for tip in feedback:
                st.write(f"- {tip}")

# -- Generator Section
st.header("🔑 Generate a Strong Password")
length = st.slider("Select password length", 8, 32, 12)

if st.button("Generate Password"):
    password, success = generate_password(length)
    if success:
        st.session_state.generated_password = password  # Save to session state to avoid losing it
        st.text(password)  # Show the password for the user
        
        # Copy to Clipboard Button (doesn't re-render)
        if st.button("Copy to Clipboard"):
            pyperclip.copy(st.session_state.generated_password)
            st.success("Password copied to clipboard!")
    else:
        st.error(password)

