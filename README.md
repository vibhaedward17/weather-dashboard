# 🌤️ Weather Analytics Dashboard

A professional-grade real-time weather tracking application built with Python. This dashboard fetches live data from the OpenWeatherMap API and provides interactive visualizations for temperature, humidity, and geographic mapping.

## 🚀 Key Features
- **Live Forecast:** Real-time 5-day weather forecasting with 3-hour precision.
- **Interactive Geospatial Mapping:** Pinpoints searched locations on an interactive map using Plotly.
- **Data Visualizations:** Dynamic line and bar charts showing temperature and humidity trends.
- **Secure Architecture:** Uses environment variables to protect sensitive API credentials.

## 🛠️ Technology Stack
- **Python** (Backend)
- **Streamlit** (Web Application Framework)
- **Plotly Express** (Interactive Analytics)
- **OpenWeatherMap API** (Data Source)
- **Python-dotenv** (Security Management)

## 🔐 Security Note
For security reasons, the `.env` file containing the API key is **not** uploaded to this repository. It is managed locally using a `.gitignore` file to ensure best practices in secret management.

## 📦 Installation & Setup
1. Clone the repository: `git clone https://github.com/vibhaedward17/weather-dashboard.git`
2. Create a `.env` file in the root directory.
3. Add your API key: `API_KEY=your_key_here`
4. Install dependencies: `pip install streamlit pandas plotly requests python-dotenv`
5. Launch the app: `streamlit run main.py`