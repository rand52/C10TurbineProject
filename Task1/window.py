import tkinter as tk
from plot import plot_data
from tkinter import simpledialog

File_Names = ['noshear TIC_veer0.2','noshear TIC_veer0.4','noshear_TIA_veer0.2','noshear_TIA_veer0.4','noshear_TIA_veer0.05','noshear_TIC_veer0.05','noTI_shear0.2_veer0.2','noTI_shear0.2_veer0.4','noTI_shear0.2_veer0.05','noTI_shear0.12_veer0.2','noTI_shear0.12_veer0.4','noTI_shear0.12_veer0.05','noveer_shear0.2_TIA','noveer_shear0.2_TIC','noveer_shear0.12_TIA','noveer_shear0.12_TIC','shear0.2','shear0.12','TIA','TIC','Uniform_noshear_noveer_noTI','veer0.2','veer0.4','veer0.05']

root = tk.Tk()
root.withdraw()

# Function to create the dataset selection window with checkboxes
def select_datasets(DataSet):
    selection_window = tk.Toplevel(root)  # Create a new window
    selection_window.title("Select Datasets")

    # Create a dictionary to hold checkbox states
    selected_datasets = {}

    # Create checkboxes for each dataset
    for filename in File_Names:
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(selection_window, text=filename, variable=checkbox_var)
        checkbox.pack(anchor='w')  # Add checkbox to the window
        selected_datasets[filename] = checkbox_var

    # Add a button to confirm selection
    def confirm_selection():
        data_list = []
        labels = []
        
        for filename, checkbox_var in selected_datasets.items():
            if checkbox_var.get():  # If the checkbox is selected
                data_list.append(DataSet[filename])
                labels.append(filename)
        
        # Close the window after selection
        selection_window.destroy()

        # Plot the selected datasets
        if data_list:
            plot_data(data_list,labels = labels, dataname = simpledialog.askstring("plot more? ", "What are you plotting? "))
            data_list = []
            labels = []

    confirm_button = tk.Button(selection_window, text="Confirm", command=confirm_selection)
    confirm_button.pack(pady=10)

    # Prevent mainloop blocking the program
    selection_window.protocol("WM_DELETE_WINDOW", selection_window.destroy)

    # Wait for the user to close the window before asking if they want to plot more
    selection_window.wait_window()