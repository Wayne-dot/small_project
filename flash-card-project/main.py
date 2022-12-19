from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(background_image, image=front_image)
    flip_timer = window.after(3000, shows_english)


def shows_english():
    canvas.itemconfig(background_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def update_list():
    # subtract the know word from the dictionary
    to_learn.remove(current_card)
    next_card()
    # write the new list and convert it into csv file
    new_frame_data = pandas.DataFrame(to_learn)
    new_frame_data.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

flip_timer = window.after(3000, shows_english)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
background_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
yes_image = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=update_list)
yes_button.grid(column=0, row=1)

no_image = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=next_card)
no_button.grid(column=1, row=1)

next_card()

window.mainloop()
