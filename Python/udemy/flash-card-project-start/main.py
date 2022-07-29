import tkinter
from tkinter import *
import pandas
import random
from pandas.core.frame import DataFrame
BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')
try:
    dat = pandas.read_csv('file.csv')
    to_learn = dat.to_dict(orient='records')
except:
    conv = DataFrame(to_learn)
    conv.to_csv('file.csv')
    
class Main:
    def cross_button(self):
        self.xy = None
        self.xy = random.choice(to_learn)
        word = self.xy['French']
        canva.itemconfig(canvas_image,image=card_front)
        canva.itemconfig(card_title,text='French',fill ='black')
        canva.itemconfig(card_name,text=word,fill ='black')
        window.after(3000,func=flash.flip)
    
    def right_button(self):
        self.cross_button()
        to_learn.remove(self.xy)
        print(len(to_learn))
        br = DataFrame(to_learn)
        br.to_csv('file.csv')
    
    def flip(self):
        word = self.xy['English']
        canva.itemconfig(canvas_image,image=card_back)
        canva.itemconfig(card_title,text='English',fill='white')
        canva.itemconfig(card_name,text=word,fill='white')


flash = Main()
window = Tk()
window.title('Flashy')
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000,func=flash.flip)

canva = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
canvas_image = canva.create_image(400,263,image=card_front)
card_title = canva.create_text(400, 150, text='Text',font=('Ariel',40,'italic'))
card_name = canva.create_text(400, 263, text='Word',font=('Ariel',60,'bold'))
canva.grid(row=0,column=0,columnspan=2)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image,highlightthickness=0,command=flash.right_button)
right_button.grid(row=1,column=1)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image,highlightthickness=0,command=flash.cross_button)
wrong_button.grid(row=1,column=0)

flash.cross_button()


window.mainloop()