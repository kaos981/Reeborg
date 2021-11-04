def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

#Con il for loop    
#for step in range(6):
    #jump()

#Con il while loop, opzione 1    
#robot = True
#while robot is not at_goal():
    #jump()
    
#Con il while loop, opzione 2    
#while at_goal() is not True:
    #jump()
    
#Con il while loop, opzione 3
#while not at_goal():
#    jump()

 
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
  
    