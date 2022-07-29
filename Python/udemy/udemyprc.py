# import random
# print("Welcome to password Generator!")
# a = int(input("How many letter would you like in your password?\n"))
# b = int(input("How many symbols would you like?\n"))
# y = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "-", "/", "_", "."]
# c =int(input("How many numbers would you like?\n"))
# g = 1
# f = 1
# d = []
# e = 1
# while(e<=a):
#     z = chr(random.randint(ord('a'), ord('z')))
#     d.append(z)
#     e = e+1
#     while(f<=b):
#         w = random.randint(0,12)
#         v = str(y[w])
#         d.append(v)
#         f=f+1
#     while(g<=c):
#         x = str(random.randint(1,9))
#         d.append(x)
#         g=g+1  
# h = len(d)
# i = 0
# print("Here is your password:")
# j = ""
# while(i<=h-1):
#     j = j + d[i]
#     i = i+1
# k = list(j)
# random.shuffle(k)
# l = 0
# m = ""
# while(l<=h-1):
#     m = m + k[l]
#     l = l+1
# print(m)


# a = "saptarshi"
# z = len(a)
# print ("You have 7 lifes")
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# k = len(stages)
# c = []
# x = 1
# yz = 0
# zx = 0
# zy =0
# while (x<=z+1):
#     c.append("_")
#     x = x+1
# print(c)
# e = len(c)
# while (True):
#     y = 0
#     d = input("Enter a Letter ")
#     b = 0
#     while(b<z):
#         if (a[b] == d):
#             n = b 
#             c[n] = d
#         else:
#            yz = y+1
#            y = yz
#         b = b + 1 
#     if (y==9):
#         zx = zy+1
#         zy = zx
#     if (zx>0 and zx<=k-1):
#         while(y>0):
#             print(stages[(k-1)-zx])
#             break
#     if (y==9):
#         print(f"You gussed {d}, that's not in the word. You lose a life. \nLife's left  {k-zx}")
#     if (zx>k-1):
#         print("You Loose")
#         break
#     i = 0
#     j = ""
#     while (i<e-1):
#         j = j + c[i]
#         i = i + 1
#     print(j)   
    
#     if (j==a):
#         break

   
# while(True):
#     def encode(a,b):
#             z = list(a)
#             x = len(z)
#             y = []
#             i = 0
#             while(i<x):
#                 c = ord(z[i])
#                 y.append(c)
#                 i = i+1
#             j = 0
#             d = []
#             jx = len(y)
#             while(j<jx):
#                 d.append(y[j]+b)
#                 j = j+1
#             d = [((item-122)+97) if item>122 else item for item in d]
#             g = 0
#             h = []
#             ha = len(d)
#             while(g<ha):
#                 h.append(chr(d[g]))
#                 g = g+1
#             gh = ""
#             gm = 0
#             gg = len(h)
#             while (gm<gg):
#                 gh = gh + h[gm]
#                 gm = gm +1
#             print(gh)
# # 122=z 97=a
#     def decode(a,b):
#         z = list(a)
#         x = len(z)
#         y = []
#         i = 0
#         while(i<x):
#             c = ord(z[i])
#             y.append(c)
#             i = i+1
#         j = 0
#         d = []
#         jx = len(y)
#         while(j<jx):
#             d.append(y[j]-b)
#             j = j+1
#         d = [(122-(97-item)) if item<97 else item for item in d]      
#         g = 0
#         h = []
#         ha = len(d)
#         while(g<ha):
#             h.append(chr(d[g]))
#             g = g+1
#             gh = ""
#             gm = 0
#             gg = len(h)
#             while (gm<gg):
#                 gh = gh + h[gm]
#                 gm = gm +1
#         print(gh)
#     s = int(input("Type '1' to encrypt, type '2' to decrypt and '3' to exit\n"))
#     if (s == 1):
#         a = input("Type your message ")
#         b = int(input("Type the shift number "))
#         encode(a,b)
#     elif (s == 2):
#         a = input("Type your message ")
#         b = int(input("Type the shift number "))
#         decode(a,b)
#     elif (s == 3):
#         break
#     else:
#         print("You entered a wrong input")
#         break 


# import os
# from typing import ItemsView
# print("Welcome to the secret auction program.")
# d = {}
# g = 0
# e = []
# while(True):
#     a = ""
#     b = 0
#     a = input("What is your name?: ")
#     b = int(input("What's your bid?: $"))
#     d.update({a:b})
#     c = input("Are there any other bidders? Type 'y' for yes or 'n' for no ")
#     if (c=='y'):
#         os.system('cls')
#     elif (c=='n'):
#         os.system('cls')
#         while (g<len(d)):
#             e.append(list(d.items())[g][1])
#             g = g+1
#         e.sort()
#         z = len(e)
#         for key, value in d.items():
#             if e[z-1] == value:
#                 print(f"The winner is {key} with a bid of ${e[z-1]}.")
#         break
  

# def add(a,b):
#     z = a+b
#     return z
# def subs(a,b):
#     z = a-b
#     return z
# def mul(a,b):
#     z = a*b
#     return z
# def div(a,b):
#     z = a/b
#     return z
# print("Welcome to calculator")
# a = int(input("Enter first number "))
# print("+\n-\n*\n/\n")
# c = input("Choose an operator: ")
# b = int(input("Enter second number "))
# if c=='+':
#     z = add(a,b)
#     print(z)
# elif c == '-':
#     z = subs(a,b)
#     print(z)
# elif c == '*':
#     z = mul(a,b)
#     print(z)
# elif c == '/':
#     z = div(a,b)
#     print(z)
# zx = 0
# zx = z
# while(True):
#     x = input(f"Press 'y' to continue calculating with {zx} else press 'n' for no ")
#     if x == 'n':
#         break
#     elif x == 'y':
#         print("+\n-\n*\n/\n")
#         m = input("Choose an operator: ")
#         n = int(input("Enter the number to be calculated with "))
#         if (m == '+'):
#             mx = add(zx,n)
#             print(mx)
#         elif m == '-':
#             mx = subs(zx,n)
#             print(mx)
#         elif m == '*':
#             mx = mul(zx,n)
#             print(mx)
#         elif m == '/':
#             mx = div(zx,n)
#             print (mx)
#     zx = mx

# import random
# a = random.randint(1,10)
# b = random.randint(1,10)
# c = []
# c.append(a)
# c.append(b)
# c.sort()
# print(f"Your cards: {c}")
# d = random.randint(1,10)
# e = random.randint(1,10)
# f = []
# f.append(d)
# f.append(e)
# f.sort()
# print(f"Computer's first card: {f[0]}")
# de = ['y', 'n']
# dh = random.choice(de)
# if (dh == 'y'):
#     df = random.randint(1,10)
#     f.append(df)
#     ed = 0
#     ey = 0
#     ex = len(f)
#     while(ed<ex):
#         ey = ey + f[ed]
#         ed = ed+1
# elif (dh == 'n'):
#     ed = 0
#     ey = 0
#     ex = len(f)
#     while(ed<ex):
#         ey = ey + f[ed]
#         ed = ed + 1
# ch = input("Press 'y' to get another card, type 'n' to pass: ")
# if (ch=='y'):
#     ab = random.randint(1,10)
#     c.append(ab)
#     z = 0
#     y = 0
#     x = len(c)
#     while(z<x):
#         y = y + c[z]
#         z = z+1
# elif ch=='n':
#     z = 0
#     y = 0
#     x = len(c)
#     while(z<x):
#         y = y + c[z]
#         z = z+1
# if ey>20:
#     print("You Win")
#     print(f"Your final hand: {c}")
#     print(f"Computer's final hand: {f}")
# elif y>20:
#     print("Computer Wins")
#     print(f"Your final hand: {c}")
#     print(f"Computer's final hand: {f}")
# if (y>ey):
#     print("You are the Winner")
#     print(f"Your final hand: {c}")
#     print(f"Computer's final hand: {f}")
# elif (ey>y):
#     print("You lost")
#     print(f"Your final hand: {c}")
#     print(f"Computer's final hand: {f}")
                 
# import random
# print("Welcome to the Number Guessing Game!")
# print("I am thinking of a number between 1 and 100")
# a = random.randint(1,100)
# b = input("Choose a difficulty. Type 'e' for easy or 'h' for hard : ")
# if b == 'e':
#     i = 10
#     ig = 0
#     while (True):
#         print(f"You have {i} attempts remaining to guess the number.")
#         c = int(input("Make a guess : "))
#         if (c>a):
#             print("Too High.")
#             if (ig<9):
#                     print("Guess Again.")
#         elif (c<a):
#             print("Too Low.")
#             if (ig<9):
#                     print("Guess Again.")
#         elif (c==a):
#             print(f"You got it! The answer was {a}")
#             break
#         elif (ig>10):
#             print("You've run out of gusses, you loose")
#             break  
#         i = i - 1
#         ig = ig + 1
# elif b == 'h':
#     i = 5
#     ig = 0
#     while True:
#         if (ig<5):
#             print(f"You have {i} attempts remaining to guess the number.")
#             c = int(input("Make a guess : "))
#             if (c>a):
#                 print("Too High.")
#                 if (ig<4):
#                     print("Guess Again.")
#             elif (c<a):
#                 print("Too Low.")
#                 if (ig<4):
#                     print("Guess Again.")
#             elif (c==a):
#                 print(f"You got it! The answer was {a}")
#                 break
#         elif (ig>5):
#             print("You've run out of gusses, you loose")
#             break   
#         i = i-1
#         ig = ig+1


#Turtle Module
#Shapes using exterior angles
# from turtle import Turtle, Screen, begin_poly
# bob_the_turtle = Turtle()
# # bob_the_turtle.shape('turtle')
# t = 0
# s = 0
# p = 0
# h = 0
# he = 0
# o = 0
# n = 0
# d = 0
# bob_the_turtle.pencolor('blue')
# while (t<3):
#     bob_the_turtle.forward(100)
#     bob_the_turtle.right(120)
#     t = t + 1
# bob_the_turtle.pencolor('brown')
# while(s<4):
#     bob_the_turtle.forward(100)
#     bob_the_turtle.right(90)
#     s = s+1
# bob_the_turtle.pencolor('red')
# while (p<5):
#     bob_the_turtle.forward(100)
#     bob_the_turtle.right(72)
#     p = p+1
# bob_the_turtle.pencolor('green')
# while(h<6):
#     bob_the_turtle.forward(100)
#     bob_the_turtle.right(60)
#     h = h+1
# bob_the_turtle.pencolor('grey')
# while (he<7):
#     bob_the_turtle.forward(100)
#     bob_the_turtle.right(51.43)
#     he = he+1
# bob_the_turtle.pencolor('sky blue')
# while(o<8):
#     bob_the_turtle.forward(100)
#     bob_the_turtle.right(45)
#     o = o + 1
# bob_the_turtle.pencolor('violet')
# while (n<9):
#     bob_the_turtle.forward(100)
#     bob_the_turtle.right(40)
#     n = n + 1
# bob_the_turtle.pencolor('yellow')
# while(d<10):
#     bob_the_turtle.forward(100)
#     bob_the_turtle.right(36)
#     d = d+1
# screen = Screen()
# screen.exitonclick()
# from turtle import Turtle, Screen, forward
# import random
# bob = Turtle()
# screen = Screen()
# screen.colormode(255)
# i = 0
# z = ['right', 'left']
# bob.pensize(5)
# bob.speed(4)
# while (i<100): 
#     a = random.randint(0,255)
#     b = random.randint(0,255)
#     c = random.randint(0,255)
#     bob.pencolor((a, b , c))
#     bob.forward(20)
#     x = random.choice(z)
#     if (x == 'right'):
#         bob.right(90)
#     elif (x == 'left'):
#         bob.left(90)
#     i = i + 1



# screen.exitonclick()

# from turtle import Turtle, Screen
# import random
# screen = Screen()
# screen.colormode(255)
# bob = Turtle()
# r = 100
# i = 0
# bob.pensize(1)
# bob.speed('fastest')
# while (i<150):
#     a = random.randint(0,255)
#     b = random.randint(0,255)
#     c = random.randint(0,255)
#     bob.pencolor((a, b , c))
#     bob.circle(r)
#     bob.left(4)
#     i = i+1
# screen.exitonclick()


