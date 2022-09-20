""" In Reeborg's World Website """
#Hurdle with For (Hurdle n2)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for passos in range(6):
    jump()


#Hurdle with While (Hurdle n3)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not_at_goal():
    if wall_infront():
        jump()
    else:
        move()

#Hurdle with Heights (Hurdle n4)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    while while_on_right():
        move()
    
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left

while not_at_goal():
    if wall_infront():
        jump()
    else:
        move()