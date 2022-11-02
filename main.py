import random
from tkinter import Tk, Canvas, PhotoImage, Button

import pandas as pandas

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    print(current_word['French'])
    canvas.itemconfig(tile_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_word['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, english_word)


def english_word():
    global current_word
    canvas.itemconfig(tile_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_word['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_word)
    print(len(to_learn))
    data_frame = pandas.DataFrame(to_learn)
    data_frame.to_csv("./data/words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, english_word)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front)
tile_text = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, "italic"))
word_text = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()
