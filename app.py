
import streamlit as st

st.set_page_config(page_title="Smart Agri & Irrigation Monitor", layout="centered")

st.title("🌾 Smart Agri & Irrigation Management")
st.subheader("Soil condition, seasonal crop recommendation, and drip irrigation monitoring")

# Sidebar inputs
st.sidebar.header("🌱 Land Details (Inputs)")
season = st.sidebar.selectbox("Season:", ["Summer", "Monsoon", "Winter"])
soil_temp = st.sidebar.slider("Soil Temperature (°C):", 15.0, 45.0, 30.0)
soil_humidity = st.sidebar.slider("Soil Humidity (%):", 10, 100, 45)
drip_percentage = st.sidebar.slider("Drip Irrigation Percentage (%):", 0, 100, 60)
st.markdown("---")
if st.button("Analyze Land & Crop"):
st.success("Analysis completed successfully!")
# 1. Seasonal crop recommendation logic
if season == "Monsoon":
best_crop = "Paddy or Maize"
water_need = "Adequate natural water available"
elif season == "Summer":
best_crop = "Watermelon or Sorghum"
water_need = "High water requirement needed!"
else:
best_crop = "Wheat or Pulses"
water_need = "Moderate water requirement"
# 2. Drip irrigation and water need determination
if drip_percentage < 50 or soil_humidity < 40:
irrigation_status = "⚠️ Warning: Low soil moisture! Turn on drip irrigation immediately (Water Needed)."
else:
irrigation_status = "✅ Land has good moisture. No water needed right now (Sufficient Moisture)."
# Display results
st.markdown("### 📊 Smart Report for Land")
st.write(f"🌱 Best Crop for this Season: {best_crop}")
st.write(f"🌡️ Soil Temperature & Humidity: {soil_temp}°C | {soil_humidity}%")
st.write(f"💧 Drip Irrigation Completion Level: {drip_percentage}%")
st.info(f"Irrigation Status: {irrigation_status}")
st.warning(f"Weather Water Need: {water_need}")