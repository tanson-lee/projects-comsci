
"""
Create a 2-player clicking game.
1. Draw an ellipse at a random location on the screen.
2. Store the location info in a variable (PVector?)
3. Using the mousePressed() function. When the user clicks,
   assign a new location to the ball.
4. Create a score variable. When the user clicks (same function above,
   add +1 to the score.
5. Display the score using the text() function.
   https://processing.org/reference/text_.html
6. Now, when the user clicks, use the mouseX and mouseY variables, within the
   mousePressed() function, compare those values to the location of the ellipse. 
   If the mouse location is within a certain range, then you add to the 
   score and change the ellipse location.
7. Add a second ball, with its own position variable, and its own score, and
   its own click detection in the mousePressed() function.
8. If a player reaches a score of 10, they win. Code this
"""

width = 500
height = 500


def setup():
    size(width, height)
    
#defining variables
ball_location_1 = PVector(width / 4, height / 2)
ball_location_2 = PVector((width * 3) / 4, height / 2)
score_1 = 0
score_2 = 0
ball_size = 100


    
def draw():
    global score
    
    #game background
    fill(0, 255, 0)
    rect(0, 0, width / 2, height)
    fill(0, 0, 255)
    rect(width / 2, 0, width / 2, height)
    
    #printing the ball
    if score_1 < 10 and score_2 < 10:
        ellipse(ball_location_1.x, ball_location_1.y, ball_size, ball_size)
        fill(0, 255, 0)
        ellipse(ball_location_2.x, ball_location_2.y, ball_size, ball_size)
    
    #printing the scores
    fill(0)
    textSize(15)
    text('Score: ' + str(score_1), (width / 2) - 80, 20)
    text('Score: ' + str(score_2), width - 80, 20)
    
    #if a player wins
    if score_2 >= 10:
        fill(0)
        textSize(32)
        text('YOU WIN PLAYER 2', (width / 2) - 130, height / 2)
        
    if score_1 >= 10:
        fill(0)
        textSize(32)
        text('YOU WIN PLAYER 1', (width / 2) - 130, height / 2)
    
def mouseClicked():
    global score_1, score_2

    
    #distance
    a = mouseX - ball_location_1.x
    b = mouseY - ball_location_1.y
    import math 
    distance = sqrt((a ** 2) + (b ** 2))
    
    #click detection
    if distance <= ball_size / 2:
        score_1 += 1
        ball_location_1.x = random(ball_size / 2, (width / 2) - 50)
        ball_location_1.y = random(ball_size / 2, height - 50)
    
    if abs(mouseX - ball_location_2.x) < ball_size / 2 and abs(mouseY - ball_location_2.y) < ball_size / 2:
        score_2 += 1
        ball_location_2.x = random((width / 2) + (ball_size / 2), width - (ball_size / 2))
        ball_location_2.y = random(ball_size / 2, height - (ball_size / 2))
