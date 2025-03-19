import turtle
import pandas as pd
from print_state import PrintState

from sympy.polys.subresultants_qq_zz import correct_sign

screen = turtle.Screen()
#back_scr = turtle.Screen()
#
screen.title("US States")
screen.register_shape("blank_states_img.gif")
# screen.addshape("blank_states_img.gif")
#
t =turtle.Turtle()
t.shape("blank_states_img.gif")
data = pd.read_csv("50_states.csv")
game_stop = False
answer_list =[]
while not game_stop:

    answer = screen.textinput("your state?", prompt="Name State").title()

    state_list =data.state.to_list()
    #correct_ans = data[data["state"].isin([answer.lower()]) == True]
    #check =correct_ans.to_string()

    if answer in state_list:
        state_name = data[data.state == answer]
        cord_x = int(state_name.x.item())
        cord_y = int(state_name.y.item())
        answer_list.append(answer)

        new= PrintState()
        new.hideturtle()
        new.cord_x = cord_x
        new.cord_y = cord_y
        new.write_state(answer)
    else:
        game_stop = True
        t.write("GAME OVER, HANNA TRY again")
    #
    # def get_mouse_click_coor(x,y):
    #    print(x,y)
    #
    # screen.onscreenclick(get_mouse_click_coor)
    #

screen.mainloop()

