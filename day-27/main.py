from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
#window.minsize(width= 500, height=300)


# user entry

input = Entry(width=10)
input.grid(column=2, row=0)

my_label = Label(text="Miles.")
my_label.grid(column=3, row = 0)

my_label = Label(text="Is equal to")
my_label.grid(column=1, row = 2)

my_label_num = Label(text="")
my_label_num.grid(column=2, row = 2)

my_label = Label(text="Km")
my_label.grid(column=3, row = 2)

# #button
#
def button_clicked():
    print("I got clicked")
    usr_input = input.get()
    new_number = str(1.6 * int(usr_input))
    my_label_num.config(text=new_number)

button = Button(text ="calculate", command = button_clicked)
button.grid(column=2, row =3)

# #Entry
#


window.mainloop()

