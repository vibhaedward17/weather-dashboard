import streamlit as st
import plotly.express as px
from backend import get_weather_data

# 1. UI CONFIGURATION
st.set_page_config(page_title="Weather Analytics", page_icon="🌤️", layout="centered")

st.title("🌤️ Weather Data Analytics")

# 2. INPUT
city = st.text_input("Enter City Name", placeholder="e.g., London, Mumbai, Tokyo")

if city:
    try:
        # Get the new combined data
        data = get_weather_data(city)

        if data:
            # 3. UNPACK DATA
            city_name = data["city"]["name"]
            lat = data["city"]["coord"]["lat"]
            lon = data["city"]["coord"]["lon"]
            forecast = data["forecast"]

            # 4. SHOW MAP (The New Feature!)
            st.subheader(f"📍 Location: {city_name}")
            
            # Create a map dataframe
            map_data = {"lat": [lat], "lon": [lon]}
            # Display the map
            st.map(map_data)

            # 5. CURRENT WEATHER
            current_temp = forecast[0]['main']['temp']
            current_desc = forecast[0]['weather'][0]['description']
            current_wind = forecast[0]['wind']['speed']

            st.markdown("### Current Conditions")
            col1, col2, col3 = st.columns(3)
            col1.metric("Temperature", f"{current_temp} °C")
            col2.metric("Wind Speed", f"{current_wind} m/s")
            col3.metric("Condition", current_desc.title())

            # 6. CHARTS
            dates = [entry['dt_txt'] for entry in forecast]
            temps = [entry['main']['temp'] for entry in forecast]
            humidity = [entry['main']['humidity'] for entry in forecast]

            st.divider()
            st.subheader("Temperature Trend")
            chart_data = {"Date": dates, "Temperature": temps, "Humidity": humidity}
            
            fig_temp = px.line(chart_data, x="Date", y="Temperature", markers=True)
            st.plotly_chart(fig_temp)

            st.subheader("Humidity")
            fig_hum = px.bar(chart_data, x="Date", y="Humidity")
            fig_hum.update_traces(marker_color='teal')
            st.plotly_chart(fig_hum)

        else:
            st.error("City not found! Please check the spelling.")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")