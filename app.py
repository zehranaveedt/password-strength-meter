import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker by Zahra Naveed", page_icon="🌘", layout="centered")

   st.markdown("""
<style>
    .main { 
        text-align: center;
    }
    
    .stTextInput {
        width: 60% !important; 
        margin: auto; 
        border: 2px solid #3498db;  /* Blue border */
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        background-color: #f3f6f9;  /* Light Grey */
        color: #2c3e50;  /* Dark Text */
    }
    
    .stButton {
        display: flex;
        justify-content: center;
    }
    
    .stButton button {
        width: 50%;
        background: linear-gradient(135deg, #2ecc71, #27ae60);  /* Green Gradient */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 12px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease-in-out;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #e74c3c, #c0392b);  /* Red Gradient */
        transform: scale(1.07);
        box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.25);
    }
</style>
""", unsafe_allow_html=True)



st.title(" 🔐 Password Strength Generator")
st.write("Enter your password below to check its security level.🔎")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ password should be **atleast 8 character long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ password should include **atleast one number (0-9) **.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include ** atleast one special character (!@#$%^&*) **.")

    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3 :
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more feature")
    else:
        st.error("❌ **Weak Password** - Follow the suggestion below to strength it.")

    #feedback
    if feedback: 
        with st.expander("🔎**Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
