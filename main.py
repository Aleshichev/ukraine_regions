import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "ukraine.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     """Получить координаты по клику"""
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("24_states.csv")
all_states = data["state"].to_list()     #создаём список штатов
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/25 області",
                                    prompt="Яка область?").title()
    if answer_state == "Вихід":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)     # через панду создаём файл
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()      #  создаём черепаху
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]     # вытащит строку которая = ответу
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

