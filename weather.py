import streamlit as st
import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_info = {
            "city": data['name'],
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }
        return weather_info
    else:
        return None

def main():
    st.title("Weather App")

    api_key = "fe97c61377545f40e42b991521c6e97f"

    city = st.text_input("Enter city name:")
    if st.button("Get Weather"):
        if city:
            weather = get_weather(api_key, city)
            if weather:
                st.success(f"Weather in {weather['city']}:")
                st.write(f"🌡️ Temperature: {weather['temperature']}°C")
                st.write(f"🌤️ Description: {weather['description'].capitalize()}")
                st.write(f"💧 Humidity: {weather['humidity']}%")
                st.write(f"🌬️ Wind Speed: {weather['wind_speed']} m/s")
            else:
                st.error("Failed to fetch weather data.")
        else:
            st.warning("Please enter a city name.")

    st.markdown("---")
    if st.button("Visit Portfolio"):
        st.markdown("[Rudransh Das](https://rudransh.rf.gd)")
        
if __name__ == "__main__":
    main()
