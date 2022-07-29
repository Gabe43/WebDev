#Doesn't end the program if there is an error "Its an error handling using try function"
import random
x = random.randint(1,100)
print ("Random Number Generated give it a Try")
while(True):
    c = int(input("Enter 1 to play and 2 to Quit"))
    if (c==1):
        x = random.randint(1,100)
        print ("Random Number Generated give it a Try")
        try:
            b=0
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
        except Exception as e:
            print(f"You entered a wrong input {e}")
    else:
        break
    