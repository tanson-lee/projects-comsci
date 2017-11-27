

def setup():
    size(400, 400)
    
def draw():
    #building
    noStroke()
    fill(255)
    rect(100, 100, 200, 300)
    
    #windows
    noStroke()
    fill(0)
    for i in range(120, 380, 50):
        rect(120, i, 20, 20)