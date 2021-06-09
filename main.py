import turtle
import pandas


data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()



screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title = f" {len(guessed_state)}/50 Guess the state", prompt = " Whats another state's name ? ").title()

    if answer_state == "Exit":
        # missing_state = []
        # for state in state_names:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        missing_state = [state for state in state_names if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break


    if answer_state in state_names:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states_to_learn.csv






screen.exitonclick()
