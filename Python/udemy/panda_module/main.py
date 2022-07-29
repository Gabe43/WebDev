import pandas
#Accessing Columns 
# data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)
# z = 0
# for item in temp_list:
#     z = z+item
# b = z/7
# print(f"Average Temperature :- {int(b)}")

# print(data['temp'].mean())
# print(data['temp'].max())
#Accessing a Row
# print(data[data.day == "Monday"])

# z = data['temp'].max()
# print (data[data.temp == z])
# monday = data[data.day == "Monday"]
# a = ((int(monday.temp)*9)/5)+32

# print(a)

# #Creating a dataframe
# data_dict = {'students': ["Sap" , "Som" , "Zee"],
#              'marks' : [65 , 53, 76]}
# data = pandas.DataFrame(data_dict)
# data.to_csv('scores.csv')
data = pandas.read_csv('Squirrel.csv')
number = data['Primary Fur Color'].to_list()
x = 0
y  = 0
z = 0
for item in number:
    if item == 'Gray':
        x = x+1
    elif item == 'Cinnamon':
        y = y+1
    elif item == 'Black':
        z = z+1


numbr_of_sq = {'Fur Color': ['Grey', 'Red', 'Black'],
                'Count': [x,y,z]}

data = pandas.DataFrame(numbr_of_sq)
data.to_csv('squirrel_count.csv')