import tkinter
from tkinter import * 
from tkinter import messagebox
import json
window = Tk()
window.minsize(width=200,height=200)
window.configure(padx=20,pady=20)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():    
    import random
    symbols = ['!','#','$','%','&','(',')','*','+']
    pas = []
    x = ''
    for item in range(0,2):
        a = random.randint(0,9)
        b = random.choice(symbols)
        pas.append(str(a))
        pas.append(str(b))
    for item in range(0,4):
        c = chr(random.randint(ord('a'),ord('z')))
        d = chr(random.randint(ord('A'),ord('Z')))
        pas.append(c)
        pas.append(d)
    random.shuffle(pas)
    for item in pas:
        x=x+item
    password.insert(0,x)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def saver():
    web = website.get()
    eml = email.get()
    passd = password.get()
    new_data = {
        web : {
            "Email": eml,
            "Password": passd
        }
    }
    if len(web) == 0 or len(passd) == 0:
        messagebox.showwarning(title='Oops', message="Please don't leave any fields empty")
    else:
        try:
            with open('file.json','r') as file:
                dxy = json.load(file)
                
        except FileNotFoundError:
            with open('file.json','w') as file:
                json.dump(new_data,file,indent=4)
        else:
            des = json.loads(open(file='file.json').read())
            if website.get() in des:
                del des[website.get()]
            dxy.update(new_data)

            with open('file.json','w') as file:
                json.dump(dxy,file,indent=4)
        finally:
            website.delete(0,END)
            password.delete(0,END)

def find_passwrd():
    xy = website.get()
    am = []
    zm = []
    dem = json.loads(open(file='file.json').read())
    if xy in dem:
        for key,value in dem[xy].items():
           am.append(key)
           zm.append(value)
    messagebox.showinfo(title=xy,message=f'{am[0]} : {zm[0]}\n{am[1]} : {zm[1]}')
           
            
            
# ---------------------------- UI SETUP ------------------------------- #
canva = Canvas(width=200,height=200)
logo = PhotoImage(file='logo.png')
canva.create_image(100,100,image=logo)
canva.grid(column=1,row=0)

#Label

web_label = Label(text = 'Website:',font=('Ariel',10,'bold'))
web_label.grid(column=0,row=1)
web_label.configure(padx=10)
email_lable = Label(text = 'Email/Username:',font=('Ariel',10,'bold'))
email_lable.grid(column=0,row=2)
email_lable.configure(padx=10)
password_label = Label(text = 'Password:',font=('Ariel',10,'bold'))
password_label.grid(column=0,row=3)
password_label.configure(padx=10)

#Entry

website = Entry(width=60)
website.grid(column=1,row=1,columnspan=1)
email = Entry(width=80)
email.insert(0,'saptarshiabhi35@gmail.com')
email.grid(column=1,row=2,columnspan=2)
password = Entry(width=60)
password.grid(column=1,row=3)

#Button

generate = Button(text='Generate Password',command=gen_pass)
generate.grid(column=2,row=3)
add = Button(text="Add",width=68,command=saver)
add.grid(column=1,row=4,columnspan=2)
search = Button(text='Search',width=15,command=find_passwrd)
search.grid(column=2,row=1)




window.mainloop()

