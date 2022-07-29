import tkinter
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canva.itemconfig(timer_text,text="0:00")
    label.config(text='Timer',font=(FONT_NAME,30,'bold'),foreground=GREEN,background=YELLOW)
    tick_1.config(text="")
    tick_2.config(text="")
    tick_3.config(text="")
    tick_4.config(text="")
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps = reps+1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps==1 or reps==3 or reps==5 or reps==7:
        count_down(work_sec)
        label.config(text='Timer',font=(FONT_NAME,30,'bold'),foreground=GREEN,background=YELLOW)
    elif reps==2 or reps==4 or reps==6:
        count_down(short_break_sec)
        label.config(text='Break',font=(FONT_NAME,30,'bold'),foreground=GREEN,background=YELLOW)
        if reps==2:
            tick_1.config(text="✓",foreground='green',background=YELLOW,highlightthickness=0)
        elif reps==4:
            tick_2.config(text="✓",foreground='green',background=YELLOW,highlightthickness=0)
        elif reps==6:
            tick_3.config(text="✓",foreground='green',background=YELLOW,highlightthickness=0)
    elif reps==8:
        count_down(long_break_sec)
        label.config(text='Break',font=(FONT_NAME,30,'bold'),foreground=GREEN,background=YELLOW)
        tick_4.config(text="✓",foreground='green',background=YELLOW,highlightthickness=0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canva.itemconfig(timer_text,text =f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
    

    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

label = Label(text='Timer',font=(FONT_NAME,30,'bold'),foreground=GREEN,background=YELLOW)
label.grid(column=1,row=0)

canva = Canvas(width=200,height=233,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canva.create_image(100,112,image=tomato)
timer_text = canva.create_text(100,130,text='0:00',fill='white',font=(FONT_NAME,25,'bold'))
canva.grid(column=1,row=1)

button = Button(text='Start',command=start_timer)
button.grid(column=0,row=2)

button_1 = Button(text='Reset',command=reset_timer)
button_1.grid(column=2,row=2)

tick_1 = Label(text="")
tick_1.place(x=100,y=300)

tick_2 = Label(text="")
tick_2.place(x=120,y=300)

tick_3 = Label(text="")
tick_3.place(x=140,y=300)

tick_4 = Label(text="")
tick_4.place(x=160,y=300)


window.mainloop()