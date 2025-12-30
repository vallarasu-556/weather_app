import tkinter as tk
from tkinter import messagebox
import requests

# Replace YOUR_API_KEY with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"


def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Enter city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        result_label.config(
            text=f"🌡 Temperature: {temp} °C\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"🌥 Condition: {desc}"
        )

    except:
        messagebox.showerror("Error", "Check internet connection")

# GUI
root = tk.Tk()
root.title("Weather App - RISE 3.0")
root.geometry("350x300")

tk.Label(root, text="Weather App", font=("Arial", 16, "bold")).pack(pady=10)

city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
