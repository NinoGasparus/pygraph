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

def updatePoints(scene):
    #scene[0].setX(time)
    #scene[0].updateSelf()
    pass
while(True):
    
    #print("\033[2J \033[?25l")
    #chrono.sleep(0.1)
    scene = []
    v = Vertex(-5,0,0)
    v.setColor(255,0,0)
    v2 = Vertex(5,0,0)
    v2.setColor(0,255,0)

    l = Line()
    l.setEnds(v,v2)
    l.setColor(255,255,0)
    

    scene.insert(0,v)
    scene.insert(0,v2)
    scene.insert(0,l)
    Rend.drawpoints(scene)
    time += 0.001


