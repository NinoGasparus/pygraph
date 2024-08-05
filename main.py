import os
import time as chrono
import random as r
import math as m
import numpy as np

from Funcs import utils 
from Primitives.Vertex import Vertex
from Primitives.Line import Line
from Setup import Setup
from Rend  import Rend
Setup.init()
Setup.setSize(-5, 5, -2, 2)

time = -5
scene = []

def updatePoints():
    scene[0].setColor(255,0,0)
    scene[3].setColor(255,0,0)
    scene[3].v1.setX(time)
print("\033[2J \033[?25l")
while(True):
    
    v = Vertex(0,0,0)
    v2 = Vertex(5,0,0)
    v.setColor(255,0,0)
    v2.setColor(0,255,0)
    

    
    l = Line()
    l.setEnds(Vertex(1,0,0),Vertex(4,0,0))
    l.calcSlope()
    scene.insert(0,l)
          
    scene.insert(0,v)
    scene.insert(0,v2)
    
    v3 = Vertex(m.cos(time), m.sin(time),0)
    scene.insert(0,v3)

    Rend.drawpoints(scene)
    updatePoints()
    time += 0.01


