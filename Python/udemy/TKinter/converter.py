import tkinter
from tkinter import *

def button_clicked():
    z = input.get()
    a = round(int(float(z)*1.60934))
    label.configure(text=a)
    

window = Tk()
window.title('Miles to Km Converter')
window.configure(padx=20,pady=20)

text = Label(text = 'Miles',font=('Ariel',10,'bold'))
text.grid(column=2,row=0)

input = Entry(width=10)
input.grid(column=1,row=0)

text_1 = Label(text= 'is equal to', font=('Ariel',10,'bold'))
text_1.grid(column=0,row=1)

text_2 = Label(text = 'Km',font=('Ariel',10,'bold'))
text_2.grid(column=2,row=1)

label = Label(text='0',font=('Ariel',10,'bold'))
label.grid(column=1,row=1)

button = Button(text='Calculate',width=10,command=button_clicked)
button.grid(column=1,row=2)



window.mainloop()