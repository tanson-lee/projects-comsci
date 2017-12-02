"""
Create a dodging game.
Ellipses will start at the top of the screen and 
fall downwards. 
The Player controls the movement of an ellipse 
at the bottom of the screen using the mouse.
The player must dodge the falling ball
Steps:
    1. Create an ellipse with its own 
    position variables. Draw it in the draw() function
    This will be the falling ball.
    2. Make this ball "fall" by giving it a y-speed.
    Update its location in the draw() function.
    Also give it an x-speed, but keep it at 0
    (unless you want to mess around a bit).
    3. When the ball hits the bottom of the screen,
    reset its position to the top of the window.
    You can assign the x-position to a random value.
    Maybe even assign the y-speed to a random value 
    as well. Also, possibly create a second falling 
    ball.
    4. Create the PLAYER ellipse with its own position
    variables. The position of the PLAYER will update
    every draw loop. In the draw loop, bind the 
    x-location variable to the mouseX variable.
    Keep this ball at the bottom of the screen. 
    Draw this ball in the draw() function.
    This will be the player.
    5. In the draw() function determine if the two
    ellipses are touching:
        a) Use pythagorean theorem to find out the 
        distance (hypotenuse) between the two origins.
        b) check to see if the distance is less than 
        the two ellipse radii. (Radiuses)
"""



width = 400
height = 400
ball_1_x = (width * 3) / 4
ball_1_y = 0
ball_1_size = 100
ball_1_speed = 1
ball_1_xspeed = 0

ball_2_x = width / 4
ball_2_y = 0
ball_2_size = 100
ball_2_speed = 1
ball_2_xspeed = 0

player_ball = 50
score = -1
seperating_line = 100
ball_fallen = 0


def setup():
    size(width, height)
    
def draw():
    global ball_fallen
    global ball_1_x, ball_1_y, ball_1_speed, ball_1_size, ball_1_xspeed
    global ball_2_x, ball_2_y, ball_2_speed, ball_2_size, ball_2_xspeed
    background(255)
    
    #boarder
    line(0, height - player_ball, width, height - player_ball)
    
    distance_1 = sqrt(abs((mouseX - ball_1_x) ** 2) + abs((height - (player_ball / 2)) - ball_1_y) ** 2)
    distance_2 = sqrt(abs((mouseX - ball_2_x) ** 2) + abs((height - (player_ball / 2)) - ball_2_y) ** 2)
    
    if distance_1 > (player_ball / 2) + (ball_1_size / 2) and distance_2 > (player_ball / 2) + (ball_2_size / 2):
        
        #1st falling ball
        if ball_1_y >= height:
            fill(0)
            ball_1_x = random(ball_1_size / 2, width - (ball_1_size / 2))
            ball_1_y = 0
            ball_1_speed = random(1, 5)
            ball_1_size = random(50, 150)
            ball_2_xspeed = random(-1, 1)
            ball_fallen += 1
        ball_1_y += ball_1_speed
        ball_1_x += ball_1_xspeed
        ellipse(ball_1_x, ball_1_y, ball_1_size, ball_1_size) 
    
        #2nd falling ball 
        if ball_2_y >= height:
            fill(0)
            ball_2_x = random(ball_2_size / 2, width - (ball_2_size / 2))
            ball_2_y = 0
            ball_2_speed = random(1, 5)
            ball_2_xspeed = random(-1, 1)
            ball_2_size = random(50, 150)
            ball_fallen += 1
        ball_2_y += ball_2_speed
        ball_2_x += ball_2_xspeed
        ellipse(ball_2_x, ball_2_y, ball_2_size, ball_2_size) 
    else:
        textSize(32)
        text('You Lose' + '\n' + 'SCORE:' + str(ball_fallen), (width / 2) - 100, height / 2)
        
    #printing score
    fill(0)
    textSize(15)
    text('SCORE: ' + str(ball_fallen), width - 100, 20)
    
    #players ball
    # if mouseY - (player_ball / 2) > (height - seperating_line):
    fill(0)
    ellipse(mouseX, height - (player_ball / 2), 50, 50)
    # else:
    #     fill(0)
    #     textSize(15)
    #     text('keep your ball below the line', (width / 2) - 100, height / 2)
        
    #collison detection
    
    import math
    
    #distance_1 = sqrt(((mouseX - ball_1_x) ** 2) + ((player_ball / 2) - ball_1_y) ** 2)
    #distance_2 = sqrt(((mouseX - ball_2_x) ** 2) + ((player_ball / 2) - ball_2_y) ** 2)
    
    #if distance_1 > (player_ball / 2) + (ball_1_size / 2) and distance_2 > (player_ball / 2) + (ball_2_size / 2):
        
    
    
    
    
    
    
    
