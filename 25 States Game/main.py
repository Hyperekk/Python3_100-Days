import turtle
import pandas as pd

score = 0
game = True
correct_guesses = []


screen = turtle.Screen()
screen.title("States Game")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

#Data
data = pd.read_csv("50_states.csv")
states = data["state"].to_list()

while len(correct_guesses) < 50:
    answer = screen.textinput(f"Score = {score}/50","Name your state:")
    answer = answer.capitalize()
    if not answer:
        new_data = pd.DataFrame(states)
        new_data.to_csv("States to learn.csv")
        break
    if answer in states:
        score += 1
        states.remove(answer)
        state = data[data.state == answer]
        writer.setpos(int(state.x),int(state.y))
        writer.write(answer)
        correct_guesses.append(answer)

#states_to_learn.csv