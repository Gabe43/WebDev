'''
#Format Function 
name = "Saptarshi"
marks = 80
phnnumbr = 6878787580
a = "The name of the student is {0}, his marks are {1} and phone number is {2}".format(name, marks, phnnumbr)
#We can also interchange the position of the variable with their positional number value ex - 0 , 1 , 2
print (a)'''

'''l = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
z = []
for item in l:
    z.append(str(item))
a =" \n ".join(z)
print (a)'''
'''
#Filter function
def by5(num):
    if num%5 == 0:
        return True
    else:
        return False
l = [1,  5, 10, 64, 78, 93, 95, 43, 54, 45, 65, 44, 25]
print (list(filter(by5, l)))'''
#Reduce Function 
from functools import reduce
l = [5,10, 3, 2, 65, 87 ,43, 32, 67, 43, 84, 78, 73]
a = reduce (max, l)
print (a)

