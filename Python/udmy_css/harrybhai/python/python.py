#z = x [::-1] We can use the [::-1] function to reverse a string

frnd_dict = {}
z = input("Enter first name")
y = input("Enter second name")
x = input("Enter third name")
w = input("Enter the last name")
a = input("Enter 1st language")
b = input("Enter 2nd language")
c = input("Enter 3rd language")
d = input("Enter 4th language")
# Like this we can input value in the dictionay from the user
frnd_dict[z] = a
frnd_dict[y] = b
frnd_dict[x] = c
frnd_dict[w] = d
print (frnd_dict)
#loops
#z = ["Apple", "Mango", "Banana", "Lichi", "Straberry"]
#for item in z:# We can use item function like this in for loop
    #print (item)
#Basic range function in for loop
#for i in range(5): #Will print numbers from 0 to 5-1 
    #print(i)
#for i in range(1, 5): #Will print numbers from 1 - 4 , we can specify the start and end using this function
    #print(i)
#@for i in range(1, 5, 2): #Will print numbers with a difference of two(Step Size)
    #print (i)
''''
for i in range(10):
    if i == 5:
         continue
        print (i)
It will not print 5 as when i =5 'It will skip thr print statement'it 
will continue and prin the next number'''    

'''multiplication table using while loop
a = int(input("Enter the number"))
b = 1
while(b<=10):
    c = a*b
    print (c)
    b=b+1

#Number Triangle, Just keeping the input in String 
a = input("Enter the number")
b = 1
while(b<=10):
    c = a*b
    print (c)
    b=b+1'''

''' Program to find prime number with break statement

a = int(input("Enter the number"))
b = 2
while (b<a):
    if(a%b == 0):
        print("It's not a Prime Number")
        break
    else:
        print("It's a Prime Number")
        break'''

'''multiplication table using for loop
a = int(input("Enter the number"))
for i in range(1, 11):
    z = a*i
    print (str(a) + "x" + str(i) + " = " +str(z))
    print (f"{a}x{i} = {z}")# We can write variable inside curly braces and it will be seen as a string'''
''' Searching the first letter and printing greetings    
    a = ["Harry" , "Kajal" , "Sheila", "Modi"]
for i in a:
    if i.startswith("S"):
        print ("Greetings")
    else:
        print ("No bro")'''

''' Factorial program and if we interchange the * with + we will get
 the sum of natural numbers from 1 to the given number

a = int(input("Enter the number"))
f = 0
for i in range(1, a+1):
    f =f*i
print (f)'''


'''Defining function using def
def heyy (e, f):
    a = e + f
    return a
x = 5
y = 6
b = int(input("Enter number"))
c = int(input("Enter number"))
d = heyy(b, c)
print (d)
def greet(name = "Stranger"): #Stranger is registered as the default name if no name is given
                              # it will take stranger
    print ("Good Morning " + name + ", Have a Great Day")
print(greet())'''

'''#Normal function using loop
def fact_loop(a):
    b = 1
    for i in range(1, a):
        b = b*(i+1)
    return b
print(fact_loop(5))
#Recursive Function
def fact_rec(a):
    if(a==1 or a==0):
            return 1
    return (a*fact_loop(a-1))
print (fact_rec(5))

'''
'''# Remove function in list made with def function
def lst_prt(a):
    if(a[0]== v):
        print([a[1],a[2],a[3]])
    elif(a[1]== v):
        print([a[0],a[2],a[3]])
    elif(a[2]== v):
        print([a[0],a[1],a[3]])
    elif(a[3]==v):
        print([a[0],a[1],a[2]])
z = input("enter")
x = input("Enter")
y = input("Enter")
w = input("Enter")
v = input("Enter the item to be removed")
f = [z, x, y, w]
print (lst_prt(f))


'''
'''My first Game "Snake, Water, Gun"
import random
def game_is(lapt,me):
    if lapt == me:
        return None
    elif lapt == "s":
        if me == "w":
            return False
        elif me== "g":
            return True
    elif lapt == "w":
        if me == "g":
            return False
        elif me == "s":
            return True
    elif lapt == "g":
        if me == "s":
            return False
        elif me == "w":
            return True
print ("Lapt's Turn : Snake (s), Water(w), Gun)(g)")
a = random.randint(1, 3)
if a == 1:
    lapt = "s"
elif a == 2:
    lapt = "w"
elif a == 3:
    lapt = "g"
b = input("My Turn : Snake (s), Water(w), Gun)(g)")
z = game_is(lapt,b)
print ("Computer Chose  " + str(lapt))
if z == None:
    print("Its a draw")
elif z:
    print("You win")
else:
    print("You lose")
'''

'''# Using open function to read a file
f = open("python.py", 'r') #if we dont mention the form it will take r as default
z = f.read() #We can also specify the number of characters to be read
print(z)
f.close()
# We can also use the .readline() function as it only reades a line
#Creating a file
z =open("fine.txt", 'w')
z.write("fine you man")
z.close()
# Append(Adding) something at the last of the text
y = open("fine.txt", 'a')
y.write(" Shit Man")
y.close()
# Automatically close the file using with statetment
with open("fine.txt", 'r') as a:
    z =a.read()
    print (z)'''

''' Creating muliple files and adding multiplication table in them 
    If we create a folder and we want to create files in it we can access it via
    FolderName/"The name we want to give the file" 
def  table_mul():
    a = 1
    while (a< 20):
        a=a+1
        print ("Table of "+ str(a) + " is :")       
        f = open("tables/Multiplication_of " + str(a), 'w')  
        b = 1
        while(b<=10):
            c = a*b
            print ( "         " + str (a) + " " + "X" + " "+ str(b) + " = " + str(c))
            f.write(str(a) + " X " + str(b) + " = " + str(c)+ "\n")
            b= b+1    
        f.close()  
z = table_mul()
print (z)'''
# .lower() function can we used to conver anything to lower case

'''Finding the line number in a log file, when the system finishes
   Reading all the lines it will return false and the loop will end
z = True
a = 1
f = open ("log.txt", 'r')
while z:
    z = f.readline()
    if "python" in z.lower():
        print ("Python is present : " + str(a))
        print (z)
    a=a+1
'''

''' After importing os we can use the function os.remove() 
    To remove a file
import os
with open ("log.txt", 'r') as f:
    z = f.read()
with open ("log_copy.txt", 'w') as b:
    x = b.write(z)
os.remove("log.txt")
+

'''
'''Armstrong number    
n = input("Enter a number")
z = len(n)
b = int(n)
x = b
r = 0 
while (b>0):
    rem = b%10
    r = r + (rem**z)
    b = b//10
if (r==x):
    print("The number is an armstrong number")
else:
    print("Its not an arm strong number")

'''





        





