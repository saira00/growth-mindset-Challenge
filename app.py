
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")

# Sidebar navigation
st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Daily Growth", "Daily Progress", "Create Account"])

# Content for each page
if page == "Home":
    st.title("💡 Growth Mindset Challenge")
    st.subheader("Understanding a Growth Mindset")
    st.write("""
    A growth mindset is about believing that skills and intelligence can improve with effort and practice.
    It helps in learning, overcoming obstacles, and staying motivated in a constantly evolving field like tech.
    """)

elif page == "Daily Growth":
    st.title("🌟 Daily Growth")
    st.write("Get motivational quotes and stories.")
    st.number_input("Pick a number", 0, 100)

elif page == "Daily Progress":
    st.title("📊 Daily Progress")
    st.write("Track your progress and set daily goals.")
    st.slider("Pick a number", 0, 100)

elif page == "Create Account":
    st.title("📝 Create Account")
    name = st.text_input("Enter your name", key="name_input")
    fname = st.text_input("Enter your father name", key="father_name_input")
    adr = st.text_area("Enter your message", key="message_input")
    
    if st.button("Done"):
        if name and fname and adr:
            st.success("✅ Your account has been created successfully!")
            st.markdown(f"""
            **Name:** {name}  
            **Father Name:** {fname}  
            **Message:** {adr}  
            """)
        else:
            st.warning("⚠️ Please fill in all fields before submitting!")

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.subheader("👩‍💻 Web Developer")
st.sidebar.write("📌 Created by: **Saira Kanwal**")
st.sidebar.write("📧 [Send Email](mailto:Sairawarisha8995@gmail.com)")
st.sidebar.write("🌐 [My Portfolio](https://your-portfolio-link.com)")
