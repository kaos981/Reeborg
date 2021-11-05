def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
infinite = 0
while not at_goal():    
    if not wall_on_right():
        turn_right()
        #infinite += infinite        
    if not wall_in_front():
        move()
    else:
        turn_left()