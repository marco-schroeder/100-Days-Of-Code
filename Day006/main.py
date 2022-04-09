def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    if wall_on_right() and front_is_clear():
        move()
    else:
        turn_left()