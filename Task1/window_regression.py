import tkinter as tk

def get_four_values():
    def submit():
        # Collect the values from the entry boxes
        val1 = entry1.get()
        val2 = entry2.get()
        val3 = entry3.get()
        val4 = entry4.get()
        values.extend([val1, val2, val3, val4])
        popup.destroy()

    popup = tk.Tk()
    popup.title("Enter the four inflow parameters")
    popup.geometry("350x200")

    values = []

    # Labels and entry boxes
    tk.Label(popup, text="Wind speed:").grid(row=0, column=0, padx=10, pady=5)
    entry1 = tk.Entry(popup)
    entry1.grid(row=0, column=1)

    tk.Label(popup, text="Turbulence intensity:").grid(row=1, column=0, padx=10, pady=5)
    entry2 = tk.Entry(popup)
    entry2.grid(row=1, column=1)

    tk.Label(popup, text="Shear:").grid(row=2, column=0, padx=10, pady=5)
    entry3 = tk.Entry(popup)
    entry3.grid(row=2, column=1)

    tk.Label(popup, text="Veer:").grid(row=3, column=0, padx=10, pady=5)
    entry4 = tk.Entry(popup)
    entry4.grid(row=3, column=1)

    # Submit button
    tk.Button(popup, text="Submit", command=submit).grid(row=4, column=0, columnspan=2, pady=10)

    popup.mainloop()
    return values


