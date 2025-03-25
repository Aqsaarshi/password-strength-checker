import streamlit as st
import re 

# Title 
st.title("🧠 Ultimate Password Strength Checker")

# Description 
st.markdown("""
    Welcome to the **Ultimate Password Strength Checker!**
    
    Ensure your password is secure by checking:
    - ✅ Length 
    - ✅ Upper & Lowercase letters
    - ✅ Numbers 
    - ✅ Special Characters 
    
    *Improve your online security by creating strong passwords!*
""")

# Input 
password = st.text_input("Enter your password:", type="password")

# Password strength check function
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check 
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & lower case check 
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one uppercase and one lowercase letter.")

    # Number check 
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one number.")

    # Special character check 
    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character.")

    return score, feedback 

# Button to check password strength
if st.button("🔘 Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)
        st.write(f"🔒 **Your password strength score is {score}/4.**")

        if score == 4:
            st.success("✅ Strong Password!")
        else:
            for tip in feedback:
                st.warning(tip)
    else:
        st.error("⚠️ Please enter a password.")


# Footer
st.markdown("""
---
Made by 👉**Aqsa Arshad Rasheed**
""")
