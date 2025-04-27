import streamlit as st

# --- Royal Mail Loyalty Program App ---
st.set_page_config(page_title="Royal Mail Loyalty Program", page_icon="🌐", layout="centered")

# --- Header ---
st.image("Royal Mail Logo (1).png", width=150)
st.title("Royal Mail Loyalty Program")

# --- Simulated Customer Data ---
customer_name = "John Doe"
loyalty_tier = "Silver Member"
points_balance = 1450
points_to_next_tier = 550

# --- Customer Overview ---
st.header(f"Welcome, {customer_name}!")
st.subheader(loyalty_tier)
st.metric(label="Points Balance", value=f"{points_balance} points")

# Progress Bar to Gold Tier
st.progress(points_balance / (points_balance + points_to_next_tier))
st.caption(f"{points_to_next_tier} points to reach Gold Tier!")

# --- Rewards Section ---
st.header("Available Rewards")

rewards = [
    {"name": "£5 Postal Credit", "cost": 500},
    {"name": "Free Delivery Upgrade", "cost": 1000},
    {"name": "Free Stamps", "cost": 750}
]

cols = st.columns(3)

for idx, reward in enumerate(rewards):
    with cols[idx % 3]:
        st.subheader(reward["name"])
        st.text(f"Cost: {reward['cost']} points")
        if st.button(f"Redeem {reward['name']}", key=idx):
            if points_balance >= reward['cost']:
                points_balance -= reward['cost']
                st.success(f"Successfully redeemed {reward['name']}!")
            else:
                st.error("Not enough points to redeem this reward.")

# --- Activity Section ---
st.header("Recent Activity")
st.write("- Redeemed: Free Stamps")
st.write("- Delivered Package: 20 April 2025")
st.write("- Tier Upgrade: Moved to Silver (March 2025)")

# Footer
st.caption("Royal Mail © 2025 Loyalty Program")
