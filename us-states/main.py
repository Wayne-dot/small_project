import turtle
import pandas
SCORE = 0

screen = turtle.Screen()
screen.title("US. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# give the corrdita that you click on the screen
# def get_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_click_coor)

response_list = []
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
game_on = True

while game_on:
    answer_state = screen.textinput(title=f"{SCORE}/50 States Correct",
                                    prompt="What's other state name?").title()
    if answer_state == "Exit":
        # states to learn.csv
        missing_state = [state for state in all_state if state not in response_list]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    # check it the answer already answer and if the answer correct
    # after type, check the answer, it it's correct, write it on locatio
    if answer_state not in response_list and answer_state in all_state:
        SCORE += 1
        my_turtle = turtle.Turtle()
        my_turtle.penup()
        my_turtle.hideturtle()
        my_turtle.pencolor("black")
        x_coor = int(data[data.state == answer_state].x)
        y_coor = int(data[data.state == answer_state].y)
        my_turtle.goto(x_coor, y_coor)
        my_turtle.write(answer_state, align="center")
        response_list.append(answer_state)



# keep the screen open
turtle.mainloop()
