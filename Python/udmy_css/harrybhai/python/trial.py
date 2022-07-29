'''class Employee:
    salary = 5000
    increment = 400
    @property
    def SalaryafterIncrement(self):
        return self.salary+ self.increment
    @SalaryafterIncrement.setter
    def SalaryafterIncrement(self,val):
        self.increment = val - self.salary 
z = Employee()
print (z.SalaryafterIncrement)
z.SalaryafterIncrement = 5600
print(z.salary)
print(z.increment)'''

'''class Complex:
    def __init__(self, num):
        self.num = num
    def __add__(self, num2):
        return self.num + num2.num
    def __mul__(self,num2):
        return self.num*num2.num
n1 = Complex(complex(7))
n2 = Complex(complex(9))
sum = n1+n2
mul = n1*n2
print (sum) 
print(mul)   '''

class Vector:
    def __init__(self, num):
        self.num = num
    def __add__(self,num2):
        return self.num + num2.num
    def __mul__(self,num2):
        return self.num*num2.num
    def __str__(self): # Used to print the object
        return f"The number is {self.num}"
    def __len__(self): #length function
        return 1
n1 = Vector(complex(7))
n2 = Vector(complex(10))
sum = n1+n2
mul = n1*n2
print (sum)
print (mul)
print(n1)
print(len(n1))



