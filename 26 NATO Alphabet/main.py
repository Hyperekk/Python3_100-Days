#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
data = pandas.read_csv("C:\\Users\\Maciej\\Desktop\\Maciej\\GitHub\\Python3_100-Days\\26 NATO Alphabet\\nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
dictionary = {row.letter:row.code for (index,row) in data.iterrows()}
# a = 0
# for letter in letters:
#     code[letter] = words[a]
#     a+=1

# print(code)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
y = True
while y:
    try:
        a = input("Input your name: ").upper()
        lista = [dictionary[word] for word in a]
    except KeyError:
        print("Only letters are allowed :)")
    else:
        y = False
        print(lista)