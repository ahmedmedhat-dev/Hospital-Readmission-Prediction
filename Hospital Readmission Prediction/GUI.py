import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib

# Load the pre-trained Random Forest model
rf_model = joblib.load('random_forest_model.pkl')


# Function to make predictions based on user input
def predict_readmission():
    try:
        # Get input values from user
        age = int(age_entry.get())
        gender = int(gender_var.get())
        time_in_hospital = int(time_in_hospital_entry.get())
        num_lab_procedures = int(num_lab_procedures_entry.get())
        num_procedures = int(num_procedures_entry.get())
        num_medications = int(num_medications_entry.get())
        num_emergency = int(num_emergency_entry.get())
        num_inpatient = int(num_inpatient_entry.get())
        num_outpatient = int(num_outpatient_entry.get())

        # Create a DataFrame for user input
        input_data = pd.DataFrame({
            'age': [age],
            'gender': [gender],
            'time_in_hospital': [time_in_hospital],
            'num_lab_procedures': [num_lab_procedures],
            'num_procedures': [num_procedures],
            'num_medications': [num_medications],
            'num_emergency': [num_emergency],
            'num_inpatient': [num_inpatient],
            'num_outpatient': [num_outpatient]
            # Add more features if needed
        })

        # Make prediction
        prediction = rf_model.predict(input_data)[0]

        # Show result
        if prediction == 1:
            messagebox.showinfo("Prediction", "The patient is likely to be readmitted.")
        else:
            messagebox.showinfo("Prediction", "The patient is not likely to be readmitted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main application window
app = tk.Tk()
app.title("Diabetes Readmission Predictor")

# Add input fields for each feature
features = [
    ("Age", 0),
    ("Gender (0=Female, 1=Male)", 1),
    ("Time in Hospital", 2),
    ("Number of Lab Procedures", 3),
    ("Number of Procedures", 4),
    ("Number of Medications", 5),
    ("Number of Emergency Visits", 6),
    ("Number of Inpatient Visits", 7),
    ("Number of Outpatient Visits", 8)
]

entries = {}
for feature, row in features:
    tk.Label(app, text=feature).grid(row=row, column=0, padx=10, pady=5)
    entry = tk.Entry(app)
    entry.grid(row=row, column=1, padx=10, pady=5)
    entries[feature] = entry

age_entry = entries["Age"]
gender_var = tk.StringVar(value="0")  # Default value for gender
tk.Radiobutton(app, text="Female", variable=gender_var, value="0").grid(row=1, column=1)
tk.Radiobutton(app, text="Male", variable=gender_var, value="1").grid(row=1, column=2)

time_in_hospital_entry = entries["Time in Hospital"]
num_lab_procedures_entry = entries["Number of Lab Procedures"]
num_procedures_entry = entries["Number of Procedures"]
num_medications_entry = entries["Number of Medications"]
num_emergency_entry = entries["Number of Emergency Visits"]
num_inpatient_entry = entries["Number of Inpatient Visits"]
num_outpatient_entry = entries["Number of Outpatient Visits"]

# Predict button
predict_btn = tk.Button(app, text="Predict Readmission", command=predict_readmission)
predict_btn.grid(row=len(features), column=0, columnspan=3, pady=10)

# Run the application
app.mainloop()