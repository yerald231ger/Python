from tkinter import *

window = Tk()
window.title("My First GUI App")
window.geometry("600x600")
window.config(padx=30, pady=30)

label = Label(text="Hello, Tkinter.", font=("Arial", 24, "bold"))
label.grid(row=0, column=0)

button = Button(text="Click me")
button.grid(row=1, column=1)

button2 = Button(text="Click me")
button2.grid(row=0, column=2)

entry = Entry()
entry.grid(row=2, column=3)



































window.mainloop()