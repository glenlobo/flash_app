import random
from tkinter import Tk, Canvas, PhotoImage, Button

import pandas as pandas

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas.create_image(400, 263, image=card_front)
tile_text = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, "italic"))
word_text = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

df = pandas.read_csv('./data/french_words.csv')
data_list = df.to_dict('records')

index = random.randint(0, 100)
print(f"{data_list[index]['French'] = }")
canvas.itemconfig(tile_text, text='French')
canvas.itemconfig(word_text, text=data_list[index]['French'])


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)


window.mainloop()
