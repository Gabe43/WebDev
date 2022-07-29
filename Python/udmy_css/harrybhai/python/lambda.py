#Virtual environment    
# to activate virtual environment :- .\nameoftheenvironment\Scripts\activate.ps1 
#We can use tab to complete it without typing the whole thing
#pip freeze is the command to find all the installed packages
#pip freeze > name.txt prints the installed software list in the txt file
#pip install -r name.txt to install all those packages present in the txt file to the virtualenv

'''func = lambda a : a+5 #Lambda function used when function is defined as an argument
x = 5
print(func(x))

#Join Function
l = ["Hello, Py"]
sent = " and " . join(l) # Adds the given term as a seperator and replaces the coma
print(sent)

#Format Function
name = "Saptarshi"
age = 20
type = "Coding"
a = "This is {0} and {2} his age is {1}" . format(name, age, type) 
 # The number is the position of the variable to be set
#It was used earlier when tgere was no f string function
print (a)'''

# Map Function


def square(n):
    return n**2


l = [5, 8, 3]
# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# Method 2 using Map Function
print(list(map(square, l)))

# Filter Function


def greater(num):
    if num > 5:
        return True
    else:
        return False

g10 = lambda num : num>10
l = [1, 89, 5, 4, 9, 6, 2, 3, 2, 4, 6, 3]
# Return the value for which the result is true
print(list(filter(greater, l)))
print(list(filter(g10 , l)))

#Reduce Function
from functools import reduce
sum = lambda a, b: a+b
l = [1,2,3,4] 
val = reduce(sum, l) #Sequencial Computation
print (val)
