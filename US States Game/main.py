import turtle
import pandas

screen = turtle.Screen()
screen. title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
names = states_data.state.to_list()

game_is_on = True
correct_guesses = []

while game_is_on:
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?")
    if answer.title() == "Exit":
        states_to_learn = []
        for element in names:
            if element not in correct_guesses:
                states_to_learn.append(element)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break
    if answer.title() in names:
       correct_guesses.append(answer)
       t = turtle.Turtle()
       t.hideturtle()
       t.penup()
       state = states_data[states_data.state == answer]
       t.goto(state.x.item(), state.y.item())
       t.write(f"{answer}")
    if len(correct_guesses) == 50:
        game_is_on = False
