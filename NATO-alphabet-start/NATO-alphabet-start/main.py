# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user input

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

#print(data)

new_dic = { value.letter: value.code for (key, value) in data.iterrows()}

usr_input = input("please enter words? :").upper()

usr_letter = [letter for letter in usr_input]

new_nato_letter =[new_dic[one_letter] for one_letter in usr_letter]
for one_letter in usr_letter:
    print(new_dic[one_letter])

#nato_letter = [ value for (key, value) in new_dic.items() if key in usr_letter]
#print(nato_letter)
# for (key, value) in new_dic.items():
#     print(key)
#     if key in usr_letter:
#         print(value)
# print(usr_letter)
# if "B" in usr_letter:
#     print("yes")