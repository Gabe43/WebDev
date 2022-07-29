'''try:
    with open("1.txt", 'r') as f:
       x = f.read()
       print (x)
except Exception as e :
    print("The file {e} is not present in the storage")

try:
    with open("2.txt", 'r') as a:
        z = a.read()
        print (z)
except Exception as g:
      print(f"The file {g} is not present in the storage")

try:
    with open("3.txt", 'r') as b:
         y = b.read()
         print(y)
except Exception as h:
      print(f"The file {h} is not present in the storage")
'''

z = [1, 5, 8, 10, 15, 80]
for index, item in enumerate(z):
    print(item)