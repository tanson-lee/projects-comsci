# x = 100
# y = 100

def setup():
    size(400, 400)
    
def draw():
    #board
    # stroke(0, 255, 0)
    # rect(100, 100, 200, 200)
    
    #squares
    times = 0
    stroke(255, 0, 0)
    for x in range(100, 288, 41):
        for y in range(100, 288, 41):
            for times in range(6):
                if times % 2 == 0:
                    fill(255)
                    rect(x, y, 41, 41)
                    times += 1
                    println('white')
                else:
                    fill(0)
                    rect(x, y, 41, 41)
                    times += 1
                    println('black')
                    
            
            # if times % 2 == 0:
            #     fill(255)
            #     rect(x, y, 41, 41)
            #     times += 1
            
            
            
            
            # if x % 2 == 0 and y % 2 == 0:
            #     fill(255)
            #     rect(x, y, 41, 41)
            
            # if (y == 100 or y == 180 or y == 260) and (x - 20) % 80 == 0:
            #     fill(255)
            # # if (y == 140 or y == 220) and x
            # else:
            #     fill(0)
            # rect(x, y, 40, 40)