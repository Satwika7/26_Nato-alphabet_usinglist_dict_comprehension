import pandas

names_data = pandas.read_csv("nato_phonetic_alphabet.csv")
names_dict = {row.letter:row.code for (index,row) in names_data.iterrows()}

user = input("enter a word")
final_names = [names_dict[item.upper()] for item in user]
print(final_names)