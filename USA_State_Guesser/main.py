import pandas as pd
import turtle

# Code to get the x, y coords on picture
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./50_states.csv", index_col="state")

states_dict = data.to_dict(orient="index")

states_guessed = []
game_is_on = True
while len(states_guessed) != len(states_dict):

    answer_state = screen.textinput(
        title=f"{len(states_guessed)}/50 Guessed",
        prompt="What's another states name?",
    ).title()

    if answer_state in states_dict.keys():
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = states_dict[answer_state]
        coordinates = list(state_info.values())
        t.goto(coordinates[0], coordinates[1])
        t.write(answer_state)
        states_guessed.append(answer_state)

    if answer_state == "Exit":
        break

states_not_guessed = pd.DataFrame(
    data=set(states_dict.keys()).difference(set(states_guessed)),
    columns=["States Not Guessed"],
)

states_not_guessed.to_csv("./states_not_guessed.csv", index_label=False)
