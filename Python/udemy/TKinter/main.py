import tkinter
from tkinter import * #Import each and every call using *

def button_clicked():
    new_text = input.get()
    print(new_text)
    my_lable.config(text=new_text)

window = Tk()
window.title('GUI')
window.minsize(width=500, height=300)

#Label
my_lable = Label(text='Lable', font=('Ariel', 24))
my_lable.grid(column=0,row=0)

#Button
button = Button(text="Click me",command=button_clicked)
button.grid(column=1,row=1)

button_2 = Button(text='Yes')
button_2.grid(column=2,row=0)

#Entry
input = Entry(width=10)
input.grid(column=3,row=2)




window.mainloop()