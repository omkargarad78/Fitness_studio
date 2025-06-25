import streamlit as st
import requests
from datetime import datetime

API_URL = "http://localhost:8000"

# Custom CSS for styling
st.markdown("""
<style>
.class-box {
    background-color: #f0f2f6;
    border-radius: 10px;
    padding: 20px;
    margin: 10px 0px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    height: 100%;
}
.class-box:hover {
    background-color: #e6e9ef;
    transform: translateY(-5px);
    transition: all 0.3s ease;
}
.class-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #0068c9;
}
.class-instructor {
    font-style: italic;
    margin-bottom: 5px;
}
.class-datetime {
    color: #5f6368;
    margin-bottom: 5px;
}
.class-slots {
    font-weight: bold;
    color: #188038;
}
</style>
""", unsafe_allow_html=True)

st.title("🏋️‍♀️ Fitness Class Booking")

page = st.sidebar.selectbox("Navigate", ["View Classes", "Book Class", "My Bookings"])

if page == "View Classes":
    st.header("Available Classes")
    res = requests.get(f"{API_URL}/classes")
    if res.status_code == 200:
        classes = res.json()
        
        # Display classes in a grid layout
        if classes:
            # Create rows with 3 columns each
            for i in range(0, len(classes), 3):
                cols = st.columns(3)
                for j in range(3):
                    if i + j < len(classes):
                        cls = classes[i + j]
                        with cols[j]:
                            # Format datetime for better display
                            try:
                                dt = datetime.fromisoformat(cls['datetime'].replace('Z', '+00:00'))
                                formatted_date = dt.strftime("%b %d, %Y at %I:%M %p")
                            except:
                                formatted_date = cls['datetime']
                                
                            # Display class in a styled box
                            st.markdown(f"""
                            <div class="class-box">
                                <div class="class-title">📌 {cls['name']}</div>
                                <div class="class-instructor">Instructor: {cls['instructor']}</div>
                                <div class="class-datetime">When: {formatted_date}</div>
                                <div class="class-slots">Available Slots: {cls['available_slots']}</div>
                                <div style="margin-top: 15px;">Class ID: {cls['id']}</div>
                            </div>
                            """, unsafe_allow_html=True)
        else:
            st.info("No classes available. Please add some classes first.")
    else:
        st.error("Failed to load classes.")

elif page == "Book Class":
    st.header("Book Your Class")
    
    # Get available classes for dropdown selection
    # Replace the number_input with this:
    res = requests.get(f"{API_URL}/classes")
    if res.status_code == 200:
        classes = res.json()
        if classes:
            class_options = {f"{c['name']} (ID: {c['id']})": c['id'] for c in classes}
            selected_class = st.selectbox("Select Class", list(class_options.keys()))
            class_id = class_options[selected_class]
        else:
            st.warning("No classes available to book. Please add classes first.")
            st.stop()
    else:
            st.error("Failed to load classes.")
            st.stop()
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")

    if st.button("Book Now"):
        if not name or not email:
            st.warning("Please fill in all fields")
        else:
            payload = {
                "class_id": class_id,
                "client_name": name,
                "client_email": email
            }
            res = requests.post(f"{API_URL}/book", json=payload)
            try:
                if res.status_code == 200:
                    st.success("Booking successful!")
                else:
                    error_msg = "Booking failed."
                    if res.text:  # Check if there's any response text
                        try:
                            error_msg = res.json().get("detail", error_msg)
                        except:
                            pass
                    st.error(error_msg)
            except Exception as e:
                st.error("An error occurred while processing your booking.")

elif page == "My Bookings":
    st.header("Check Your Bookings")
    email = st.text_input("Enter your email")
    if st.button("Get Bookings"):
        if not email:
            st.warning("Please enter your email")
        else:
            res = requests.get(f"{API_URL}/bookings", params={"email": email})
            if res.status_code == 200:
                bookings = res.json()
                if bookings:
                    for i in range(0, len(bookings), 2):
                        cols = st.columns(2)
                        for j in range(2):
                            if i + j < len(bookings):
                                b = bookings[i + j]
                                with cols[j]:
                                    st.markdown(f"""
                                    <div class="class-box">
                                        <div class="class-title">✅ Booking Confirmed</div>
                                        <div class="class-instructor">Name: {b['client_name']}</div>
                                        <div>Class ID: {b['class_id']}</div>
                                    </div>
                                    """, unsafe_allow_html=True)
                else:
                    st.info("No bookings found for this email.")
            else:
                st.error("Failed to load bookings.")
