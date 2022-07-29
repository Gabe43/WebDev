a = { 1 ,2 , 3, 4, 5}
''' But if we put a = {1 , 2 , 3 , 4 , 5 , 2 }
    It will ignore the last two because sets doesn't
    Repeat itselt''' 
print (type(a))
print (a)
''' Important : This Syntax will create and empty Dictionary and
    Not an empty Set  '''
b = {}
print (type(b)) # This will print Dictionary as the type
# Empty Set 
c = set()
print (type(c)) # This will print an empty set
c.add(4) # Adding value to an empty set
c.add(6)
# c.add([4, 5, 6]) ; c.add({4 : 5}) Will not be added because list  and dictionary cannot be added in a set
c.add((4, 5, 6)) #tuple can be added in set
print (c)
print (len(c)) # Prints the length of the set
c.remove(6) # Removes the target number
print (c.pop()) # Removes a random number 
# c.clear() Empties the set
#c.union() Returns all items from both sets 
# #c.intersection() Returns matching items in both sets
