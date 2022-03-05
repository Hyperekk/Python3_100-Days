import tkinter

def button_clicked():
    label.config(text = entry.get())

window = tkinter.Tk()
window.title("GUI")
window.minsize(500,300)
window.config(padx=20,pady=20)


label = tkinter.Label(text="Example of label",font=("Arial",24))
label["text"] = "Text"
label.grid(column=1,row=1)

button = tkinter.Button(text="Change text",command=button_clicked)
button.grid(column=2,row=2)

button = tkinter.Button(text="OK",width=10)
button.grid(column=3,row=1)

entry = tkinter.Entry(width=20)
entry.grid(column=4,row=4)



window.mainloop()