from tkinter import *

def change_text():
    mile = int(entry.get())
    km = mile * 1.6
    label2.config(text=round(km,2),padx=5)

window = Tk()
window.title("Converter")
window.minsize(width=500,height=100)
window.config(padx=30,pady=30)

entry = Entry(width=10)
entry.grid(column=1,row=1)

label1 = Label()
label1.config(text="Miles is equal to ",padx=5)
label1.grid(column=2,row=1)

label2 = Label()
label2.config(text="0",padx=5)
label2.grid(column=3,row=1)

label3 = Label()
label3.config(text="Km",padx=5)
label3.grid(column=4,row=1)

button = Button(text="Calculate",width=10,command=change_text)
button.grid(column=5,row=1)


window.mainloop()
