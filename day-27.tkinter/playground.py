# import tkinter
# import turtle

# window = tkinter.Tk()

# window.title("My First GUI App")
# window.geometry("720x720")
# window.minsize(720, 720)

# # Label
# count = 0
# label = tkinter.Label(text=f"Hello, Tkinter.", font=("Arial", 24, "bold"))
# label.pack(side="left")

def add(*args):
    for n in args:
        print(n)

add(1, 2, 3, 4, 5)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


# window.mainloop()