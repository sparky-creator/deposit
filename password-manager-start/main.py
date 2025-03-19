from tkinter import *
from tkinter import messagebox

PINK = "#C599B6"
RED = "#E6B2BA"
GREEN = "#FFDCCC"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 12,"bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    with open("pass_word.txt", mode="a") as docu:
        docu.write(f"{website_entry.get() } | {email_entry.get()} | {password_entry.get() } \n")

        website_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=RED)

canvas = Canvas(width=300, height=300, highlightthickness=0)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image= photo_image)
canvas.grid(column=0,row=1, columnspan=4)

website_label = Label(text= "website",bg=PINK ,font=FONT_NAME)
website_label.grid(column=0,row=2)

email_label = Label(text= "email/usr name",bg=PINK , font=FONT_NAME)
email_label.grid(column=0,row=3)

password_label = Label(text= "password",bg=PINK , font=FONT_NAME)
password_label.grid(column=0,row=4)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=2)
email_entry = Entry(width=35)
email_entry.insert(0,"jepark820@gmail.com")
email_entry.grid(column=1, row=3 )
password_entry = Entry(width=21)
password_entry.grid(column=1, row=4 )


generate_password_button = Button(text="Generate Password", bg=GREEN)
generate_password_button.grid(column=2, row=4)

add_button = Button(text="Add", bg=GREEN, command=save_password)
add_button.grid(row=5, column=1)

window.mainloop()