import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

letters = data['letter'].to_list()
code  = data['code'].to_list()

dict = {letters[item]:code[item] for item in range(0,len(letters))}

txt = input("Enter your Name").upper()
txt_ls = [item for item in txt]
xz = []
for item in txt_ls:
    for key,value in dict.items():
        if item == key:
            z = value
            xz.append(z)

print(xz)
        
