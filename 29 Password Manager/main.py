from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    mail = email_entry.get().strip()
    password = password_entry.get().strip()
    website = website_entry.get().strip()

    if not website or not password:
        messagebox.showerror(title="Error",message="One or more of the fields are empy.")
        return

    is_ok = messagebox.askokcancel(title="Details",message=f"Your details: \nEmail: {mail} "
                                                    f"\nPassword: {password}\nSave?")

    if is_ok:
        with open("data.txt","a") as f:
            f.write(f"{website} | {mail} | {password} \n")

        password_entry.delete(0,END)
        website_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=1,column=2)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=2,column=1)

email = Label(text="Email/Username:")
email.grid(row=3,column=1)

password_label = Label(text="Password:")
password_label.grid(row=4,column=1)

#Entries
website_entry = Entry(width=52)
website_entry.grid(row=2,column=2,columnspan=2,sticky="w")
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=3,column=2,columnspan=2,sticky="w")
email_entry.insert(0, "email@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(row=4,column=2,sticky="w")

#Buttons
password_button = Button(text="Generate Password",command=pass_gen)
password_button.grid(row=4,column=3,sticky="w")

add_button = Button(text="Add",width=44,command=save_pass)
add_button.grid(row=5,column=2,columnspan=2)


window.mainloop()