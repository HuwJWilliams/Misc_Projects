import pandas as pd

data = pd.read_csv("./nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

answer = input("What would you like to say?\n")

result = [nato_dict[letter] for letter in answer.upper()]
print(result)
