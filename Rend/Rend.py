from  Setup import Setup
import numpy as np
from Setup import  Setup
from Funcs import utils
mts = utils.mts
yshrink= Setup.yshrink


screensize = Setup.screensize

def drawpoints(scene):
	print("\033[?25l", end ="")
	print("\033[30m", end ="")
	#drawing points, lines etc
	
	for i in scene:
		if i.visible:
			match i.type:
				case "vertex":
					print(i.color, end = "")
					placePoint(i.sx, i.sy)
					print("\033[30m", end="")

				case "line":
					print(i.color, end="")
					plotLine(i)
				case "triangle":
					print(i.color, end="")
					refPoint = i.l1.v1
					refLine = i.l2

					for j in np.arange(0,refLine.lenght, 0.05):
						planeX = refLine.v1.x+(j*refLine.dx)
						planeY = refLine.v1.y+(j*refLine.dy)
						tmpLine = Line();
						tmpV = Vertex(planeX, planeY, 0)
						tmpLine.setEnds(tmpV, refPoint)
						tmpLine.calcSlope()

						for k in np.arange(0, tmpLine.lenght, 0.05):
							planex = tmpLine.v1.x+(k*tmpLine.dx)
							planey = tmpLine.v1.y+(k*tmpLine.dy)
							screenPoint = mts(planex, planey)
							placePoint(screenPoint[0],screenPoint[1])

def placePoint(sx, sy):
	print(f"\033[{sy};{sx}H", end="")
	print("\u2588", end="")
	ssx = screensize["x"]
	ssy = screensize["y"]

	print(f"\033[{ssx};{ssy}H", end="")


def plotLine(i):
	for j in np.arange(0, i.lenght, 0.05):
		planeX = i.v1.x +( j * i.dx)
		planeY = i.v1.y +( j * i.dy) * yshrink
		
		screenPoint = mts(planeX, planeY)
		if(not screenPoint == None):
			placePoint(screenPoint[0],screenPoint[1])




