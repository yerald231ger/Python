from tkinter import *

window = Tk()
window.title("My First GUI App")
window.geometry("400x150")
window.config(padx=30, pady=30)

# Prevent window resizing
window.resizable(False, False)

# Create Entry and Labels
miles_entry = Entry()
label = Label(text="Miles")
label2 = Label(text="is equal to")
km_result_label = Label(text="0")
km_label = Label(text="Km")

# Create Button
button = Button(text="Calculate")

# Define the calculation function
def on_calculate():
    miles = float(miles_entry.get())
    km = miles * 1.60934
    km_result_label.config(text=f"{km}")

# Configure button command
button.config(command=on_calculate)

# Arrange widgets using grid
miles_entry.grid(row=0, column=1)
label.grid(row=0, column=2)
label2.grid(row=1, column=0)
km_result_label.grid(row=1, column=1)
km_label.grid(row=1, column=2)
button.grid(row=2, column=1)

window.mainloop()








