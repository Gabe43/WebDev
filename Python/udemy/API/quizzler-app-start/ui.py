import tkinter
from tkinter import *
from question_model import Question
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class Quiz_Interface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.interface()
    
    def interface(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20)
        self.window.config(background=THEME_COLOR)
        
        self.scor = Label(text='Score: 0',foreground='white',background=THEME_COLOR)
        self.scor.grid(row=0,column=1)
        
        self.canvas = Canvas(width=300,height=250,background='white')
        self.question_text = self.canvas.create_text(150,125,text='Question',fill=THEME_COLOR,font=('Ariel',20,'italic'),width=280,)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        right_image = PhotoImage(file='images/true.png')
        self.right = Button(image=right_image,command=self.right_button)
        self.right.grid(row=2,column=0)

        wrong_image = PhotoImage(file='images/false.png')
        self.wrong = Button(image=wrong_image,command=self.wrong_button)
        self.wrong.grid(row=2,column=1)
        
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.scor.config(text=f'Score: {self.quiz.score}',font=('Ariel',20,'bold'))
            q_text =  self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='You have reached the end of the Quiz')
            self.right.config(state='disabled')
            self.wrong.config(state='disabled')

    def right_button(self):
        ans = 'True'
        value = self.quiz.check_answer(ans)
        if value==True:
            self.canvas.config(background='green')
        elif value == False:
            self.canvas.config(background='red')
        self.window.after(1000,self.next_question)
        
                        
    def wrong_button(self):
        ans = 'False'
        value = self.quiz.check_answer(ans)
        if value==True:
            self.canvas.config(background='green')
        elif value == False:
            self.canvas.config(background='red')
        self.window.after(1000,self.next_question)
            
        
    
    
