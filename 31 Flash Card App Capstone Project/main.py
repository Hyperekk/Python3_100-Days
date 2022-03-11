BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from pandas import *
import random

#Function - Saving words
def is_known():
    data_dict.remove(random_word)
    data = DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv",index=False)
    new_word()


#Function - Change side
def change_side():
    canvas.itemconfig(canva_image,image=back_img)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=random_word["English"],fill="white")

#Function - Change word on card
def new_word():
    global random_word
    random_word = random.choice(data_dict)
    canvas.itemconfig(canva_image,image=front_img)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=random_word["French"],fill="black")
    window.after(3000,change_side)


#Getting Data
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

#Creating window
window = Tk()
window.title("Flash card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(width=800,height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canva_image = canvas.create_image(400,263,image=front_img)
title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=1,column=1,columnspan=2)


#Buttons
x_image = PhotoImage(file="images/wrong.png")
xbutton = Button(image=x_image, highlightthickness=0,command=new_word)
xbutton.grid(row=2,column=1)

y_image = PhotoImage(file="images/right.png")
ybutton = Button(image=y_image, highlightthickness=0,command=is_known)
ybutton.grid(row=2,column=2)


new_word()

window.mainloop()
