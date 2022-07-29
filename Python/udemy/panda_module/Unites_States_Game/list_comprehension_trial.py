#To find the common numbers in two list and creating a new list with them
with open('file2.txt') as file:
    z = file.readlines()
    t = [int(n)for n in z]
print(t)
with open('file1.txt') as fil:
    x = fil.readlines()
    y = [int(m) for m in x]
print(y)
ty = [item for item in y if item == item in t] #My Way 
# ty = [item for item in y if item in t] #Udemy's Way

print(ty)

#We can loop through pandas items using the itterrow function
student_dict = {
    "students" : ["Sap", "Sam", "Zee"],
    "score" : [56, 76, 98]
}
import pandas
new_trial = pandas.DataFrame(student_dict)
print(new_trial)

for (index, row) in new_trial.iterrows():
    print(row)
