import tkinter as tk
from tkinter import ttk

# Function that runs when button is clicked
def predict_price():
    bedrooms = bedrooms_entry.get()
    bathrooms = bathrooms_entry.get()
    sqft = sqft_entry.get()
    
    # Placeholder prediction
    result_label.config(
        text=f"Prediction would be calculated here\n"
             f"Bedrooms: {bedrooms}, Bathrooms: {bathrooms}, Sq Ft: {sqft}"
    )

# Create window
root = tk.Tk()
root.title("House Price Predictor")
root.geometry("500x400")

# Title
title_label = tk.Label(
    root,
    text="House Price Predictor",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Bedrooms
tk.Label(input_frame, text="Bedrooms:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
bedrooms_entry = tk.Entry(input_frame)
bedrooms_entry.grid(row=0, column=1, padx=10, pady=5)

# Bathrooms
tk.Label(input_frame, text="Bathrooms:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
bathrooms_entry = tk.Entry(input_frame)
bathrooms_entry.grid(row=1, column=1, padx=10, pady=5)

# Square Footage
tk.Label(input_frame, text="Square Footage:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
sqft_entry = tk.Entry(input_frame)
sqft_entry.grid(row=2, column=1, padx=10, pady=5)

# Predict button
predict_button = ttk.Button(
    root,
    text="Predict Price",
    command=predict_price
)
predict_button.pack(pady=20)

# Result area
result_label = tk.Label(
    root,
    text="Enter house information and click Predict",
    font=("Arial", 12)
)
result_label.pack(pady=20)

root.mainloop()