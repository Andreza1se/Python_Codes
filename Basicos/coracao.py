import math
from turtle import *

def CoracaoA(Y):

    return 12*math.sin(Y)**3

def CoracaoB(X):
    return 12*math.cos(X)-5*\
    math.cos(2*X)-2*\
        math.cos(3*X)-\
        math.cos(4*X)
speed(0)

bgcolor("pink")

for i in range(100000):
    goto(CoracaoA(i)*20, CoracaoB(i)*20)
    for j in range(5):
        color("black")
    goto(0,0)
    done    