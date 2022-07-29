import random
x = random.randint(1,100)
print (x)
print ("Random Number Generated give it a Try")
b = 0
while (b<=50):
    a = int(input("Enter the number"))
    if (a<x):
        print("Enter a Bigger Number")
    elif (a>x):
        print("Enter a Smaller Number")
    elif (a==x):
        print(f"You guessed correctly in {b+1} tries")
        break
    b=b+1
with open("Highscore.txt", 'r') as f:
    highscore = int (f.read())
if (b<highscore):
    print("You have broken the highest score")
    with open("Highscore.txt", 'w') as f:
         f.write(str(b+1))



