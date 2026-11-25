import tkinter as tk
from tkinter import ttk
import warnings
import joblib

'''This file does not import pandas (so that anyone else running this file does not have to dowload the library).This means that user inputs are not passed to the model in a dataframe. This causes a warning to be displayed since feature names are not provided. The model still works an can take user inputs. The only real 'danger' is that arguments could be passed to the model in the wrong order. Since the scope of this project is rather small this is not a major issue as the argument order can be maintained manually. The code below stops this specific warning from appearing every tme the code is run.'''
warnings.filterwarnings(
    "ignore",
    message="X does not have valid feature names"
)

#Load the model and predictors in
model = joblib.load("house_price_model.pkl")
predictors = joblib.load("predictors.pkl")

#Predictor order: ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'yr_built', 'lat', 'long', 'sqft_basement', 'waterfront', 'renovated', 'view', 'condition', 'grade']

def initializePredictors():
    data = {}
    for p in predictors:
        data[p]=None
   
    return data

#Convert the user input data into a list in the correct order to be processed by the model
def format(data):
    formatted = []
    for p in predictors:
        formatted.append(p)

    for i in range(len(formatted)):
        input = data[formatted[i]]
        formatted[i] = input

    return formatted

#Function that runs when predict button is clicked
def predict_price():
    user_data = initializePredictors()
    formatted_user_data = format(user_data)

    bedrooms = bedrooms_entry.get()
    bathrooms = bathrooms_entry.get()
    sqft = sqft_entry.get()
    #price = model.predict(user_data)
    if None in formatted_user_data:
        result_label.config(
            text=f"Please fill all input fields"
        )
    else:
        # Placeholder prediction
        result_label.config(
            text=f"Prediction would be calculated here\n"
                f"Bedrooms: {bedrooms}, Bathrooms: {bathrooms}, Sq Ft: {sqft}\n"
                #f"{price}"
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