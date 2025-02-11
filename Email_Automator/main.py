PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in names:
    name = name.strip("\n")
    new_letter = letter.replace(PLACEHOLDER, name)
    with open(f"./output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(new_letter)
