import streamlit as st

st.set_page_config(page_title="Loyalty Coupon App", layout="centered")

# Dummy coupon list
coupons = [
    {"id": 1, "title": "10% Off"},
    {"id": 2, "title": "Free Coffee"},
    {"id": 3, "title": "Buy 1 Get 1 Free"},
]

# Initialize session state
if "user" not in st.session_state:
    st.session_state.user = None
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# --- User Entry Section ---
st.title("🎉 Loyalty Coupon Program")

if st.session_state.user is None:
    user_input = st.text_input("Enter your name or email:")
    if st.button("Start"):
        if user_input:
            st.session_state.user = user_input
            if user_input not in st.session_state.user_data:
                st.session_state.user_data[user_input] = {"coupons": [], "points": 0}
        else:
            st.warning("Please enter a valid name or email.")

# --- Coupon Collection Section ---
else:
    st.subheader(f"Welcome, {st.session_state.user}!")
    user_info = st.session_state.user_data[st.session_state.user]

    st.markdown("### Available Coupons")
    for c in coupons:
        collected = c["id"] in user_info["coupons"]
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{c['title']}**")
        with col2:
            if collected:
                st.success("Collected")
            else:
                if st.button("Collect", key=f"collect_{c['id']}"):
                    user_info["coupons"].append(c["id"])
                    user_info["points"] += 1
                    st.experimental_rerun()

    # Loyalty Progress
    st.markdown("### 🎯 Loyalty Points")
    st.info(f"You have {user_info['points']} point(s).")

    # Example reward logic
    if user_info["points"] >= 5:
        st.success("🎁 You’ve earned a reward! Redeem at the counter.")
    
    if st.button("🔁 Log out"):
        st.session_state.user = None
