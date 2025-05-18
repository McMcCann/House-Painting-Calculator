import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("500x500")
root.title("House Painting Calculator")

#Data
States = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

Cost_Per_Sqft_by_State = {
    "Alabama": 2.00,
    "Alaska": 3.50,
    "Arizona": 2.25,
    "Arkansas": 2.00,
    "California": 3.50,
    "Colorado": 2.75,
    "Connecticut": 3.25,
    "Delaware": 2.75,
    "Florida": 2.50,
    "Georgia": 2.25,
    "Hawaii": 3.75,
    "Idaho": 2.25,
    "Illinois": 2.75,
    "Indiana": 2.25,
    "Iowa": 2.00,
    "Kansas": 2.00,
    "Kentucky": 2.00,
    "Louisiana": 2.25,
    "Maine": 2.75,
    "Maryland": 3.00,
    "Massachusetts": 3.25,
    "Michigan": 2.50,
    "Minnesota": 2.50,
    "Mississippi": 2.00,
    "Missouri": 2.25,
    "Montana": 2.25,
    "Nebraska": 2.00,
    "Nevada": 2.50,
    "New Hampshire": 2.75,
    "New Jersey": 3.25,
    "New Mexico": 2.25,
    "New York": 3.50,
    "North Carolina": 2.50,
    "North Dakota": 2.00,
    "Ohio": 2.25,
    "Oklahoma": 2.00,
    "Oregon": 2.75,
    "Pennsylvania": 2.75,
    "Rhode Island": 3.00,
    "South Carolina": 2.25,
    "South Dakota": 2.00,
    "Tennessee": 2.25,
    "Texas": 2.25,
    "Utah": 2.50,
    "Vermont": 2.75,
    "Virginia": 2.75,
    "Washington": 3.00,
    "West Virginia": 2.00,
    "Wisconsin": 2.25,
    "Wyoming": 2.00,
}


label = tk.Label(root, text="House Painting Calculator", font="Arial 20 bold")
label.pack(padx = 20, pady = 20)

label = tk.Label(root, text="Enter square footage of the surface in square feet:")
label.pack(padx = 10, pady = 10)
footage_entry = tk.Entry(root)
footage_entry.pack(padx = 10, pady = 10)

label = tk.Label(root, text="What State do you live in:")
label.pack(padx = 10, pady = 10)
state_entry = ttk.Combobox(root, values=States)
state_entry.pack(padx = 10, pady = 10)

#Save Inputs
def save_info():
    house_footage = footage_entry.get()
    state = state_entry.get()
    print(house_footage, state)
    Cost = Cost_Per_Sqft_by_State.get(state)
    print(Cost)
    Total_Cost = float(house_footage) * float(Cost)

    label = tk.Label(root, text="Total Cost: "+ str(Total_Cost))
    label.pack(padx = 10, pady = 10)
    return 
                     
button = tk.Button(root, text="Calculate", font="Arial 14 bold", bg="green", command=save_info)
button.pack(padx = 10, pady = 15)




root.mainloop()