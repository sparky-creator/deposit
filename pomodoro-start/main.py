from tkinter import *
import math as m
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button_clicked():
    global REPS
    REPS +=1
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
    elif REPS % 2 ==0:
        count_down((SHORT_BREAK_MIN*60))
    else:
        count_down(WORK_MIN*60)

    print("I got clicked")
    count_down(15)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = m.floor(count /60)
    count_sec = count % 60

    # if count_sec == 0 :
    #     count_sec ="00"

    if count_sec < 10:
        count_sec =f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count -1)
    else:
        start_button_clicked()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=99, pady=50, bg=YELLOW)


header_letter = Label(text="TIMER", fg=GREEN,bg=YELLOW ,font=(FONT_NAME, 35,"bold"))
header_letter.grid(column=2, row=1)

canvas = Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image= photo_image)
timer_text = canvas.create_text(103,130, text="00:00",fill="white", font=(FONT_NAME, 35,"bold"))

canvas.grid(column=2, row=2)



start_button = Button(text ="Start", command = start_button_clicked)
start_button.grid(column=1, row =3)

def reset_button_clicked():
    print("I got clicked")

reset_button = Button(text ="Reset", command = reset_button_clicked)
reset_button.grid(column=3, row =3)

check_letter = Label(text="✔", fg=GREEN,bg=YELLOW ,font=(FONT_NAME, 25,"bold"))
check_letter.grid(column=2, row=4)

window.mainloop()
