
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

ball_location_1 = PVector(100, 200)
ball_location_2 = PVector(300, 200)
score_1 = 0
score_2 = 0

def setup():
    size(400, 400)
    
def draw():
    global score
    fill(0, 255, 0)
    rect(0, 0, 200, 400)
    fill(0, 0, 255)
    rect(200, 0, 200, 400)
    
    ellipse(ball_location_1.x, ball_location_1.y, 100, 100)
    fill(0, 255, 0)
    ellipse(ball_location_2.x, ball_location_2.y, 100, 100)
    
    fill(0)
    textSize(15)
    text('Score: ' + str(score_1), 130, 20)
    text('Score: ' + str(score_2), 330, 20)
    
    if score_2 >= 10:
        fill(0)
        textSize(32)
        text('YOU WIN PLAYER 2', 70, 200)
        
    if score_1 >= 10:
        fill(0)
        textSize(32)
        text('YOU WIN PLAYER 1', 70, 200)
    
def mouseClicked():
    global score_1
    
    # random_x = random(50, 150)
    # random_y = random(50, 350)
    # ball_location.x = random_x
    # ball_location.y = random_y
    
    if abs(mouseX - ball_location_1.x) < 50 and abs(mouseY - ball_location_1.y) < 50:
        score_1 += 1
        ball_location_1.x = random(50, (width / 2) - 50)
        ball_location_1.y = random(50, height - 50)

    
    global score_2
    
    # random_x = random(50, 150)
    # random_y = random(50, 350)
    # ball_location.x = random_x
    # ball_location.y = random_y
    
    if abs(mouseX - ball_location_2.x) < 50 and abs(mouseY - ball_location_2.y) < 50:
        score_2 += 1
        ball_location_2.x = random(250, 150)
        ball_location_2.y = random(250, 350)
        
  
    
    
    # if (mouseX in range(int(random_x - 50), int(random_y + 50))) and (mouseY in range(int(random_y - 50), int(random_y + 50))):
    #     score += 1
