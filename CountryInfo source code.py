import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests

def get_countries_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if isinstance(data, list) and data:  # Check if data is a non-empty list
            country_data = data[0]
            information_dict = {
                "Capital": country_data.get("capital", ['N/A'])[0],
                "Population": country_data.get("population", 'N/A'),
                "Area": country_data.get("area", 'N/A'),
                "Region": country_data.get("region", 'N/A'),
                "Subregion": country_data.get("subregion", 'N/A'),
                "Languages": ", ".join(country_data.get("languages", {}).values())
            }
            return information_dict
        else:
            print(f"No country found by the name '{country_name}'")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def show_country_info():
    country_name = entry_country.get()
    if not country_name:
        messagebox.showwarning("Input Error", "Please enter a country name.")
        return
    
    country_info = get_countries_info(country_name)
    
    if country_info:
        info = f"Details about {country_name.capitalize()}:\n\n"
        for key, value in country_info.items():
            info += f"{key}: {value}\n"
        # messagebox.showinfo("Country Information", info)

        info_label = tk.Label(root, text=info,font=("Arial", 9))
        info_label.place(x = 150, y=220, height=200, width= 200)
    else:
        messagebox.showerror("Name error", f"No country found by the name {country_name}")

# Setting up the main window
root = tk.Tk()
root.title("Country Info")
root.geometry("488x400")
root.config(bg = "#00171f")

# Label for country name input
label = tk.Label(root, text="Enter the country name ",font=("Arial", 14),bg = "#00171f", fg = 'white')
label.place(x = 150, y=50, width=200)

# Entry widget for country name
entry_country = tk.Entry(root, width=40,font=("Arial black", 10))
entry_country.place(x = 100, y=120, width = 150 , height = 50)
entry_country.focus_set()

# Button to get country information
button = tk.Button(root, text="Get Info",font=("Arial bold", 10), command=show_country_info, bg = "#00a8e8")
button.place(x = 250, y=120, width = 150 , height = 52)

# Start the GUI event loop
root.mainloop()