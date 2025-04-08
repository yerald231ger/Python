import os
import time
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}   

try:
    data = pd.read_csv("day-31.capstone/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("day-31.capstone/data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text="Spanish", fill="white")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)
    
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("day-31.capstone/data/words_to_learn.csv", index=False)
    next_card()
    
flip_timer = window.after(3000, next_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="day-31.capstone/images/card_front.png")
card_back_img = PhotoImage(file="day-31.capstone/images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)    
canvas.grid(row=0, column=0, columnspan=2)    

cross_image = PhotoImage(file="day-31.capstone/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.config(bg=BACKGROUND_COLOR, borderwidth=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="day-31.capstone/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.config(bg=BACKGROUND_COLOR, borderwidth=0)
known_button.grid(row=1, column=1)


next_card()




window.mainloop()