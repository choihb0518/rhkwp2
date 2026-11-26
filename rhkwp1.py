import turtle
import time
turtle.speed(0)
j=10
l=60
turtle.shapesize(1)
for c in range(10):
        for a in range(6):
            for colours in ["red","orange","yellow","green","blue","purple"]:
                turtle.color(colours)
                turtle.left(60.5)
                turtle.forward(j)
                j+=1
        l-=0.5
time.sleep(20)