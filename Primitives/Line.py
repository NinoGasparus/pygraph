import math as m
class Line:
	def __init__(self):
		self.v1 = None
		self.v2 = None
		self.dx = None
		self.dy = None
		self.stepResolution = 1
		self.visible = False
		self.type = "line"
		self.lenght = 0
		self.color = "\033[38;2;0;255;0m"
		self.depth = 0
	def setEnds(self, v1, v2):
		self.v1 = v1
		self.v2 = v2
		self.lenght = m.sqrt((self.v1.x-self.v2.x)**2 + (self.v1.y-self.v2.y)**2)
		self.calcSlope()
		self.visCheck()



	def calcSlope(self):
		self.stepResolution = self.lenght
		self.dx = -(self.v1.x - self.v2.x)/self.stepResolution
		self.dy = (self.v1.y - self.v2.y)/self.stepResolution
	
	def visCheck(self):
		if( not self.v1.visible and not self.v2.visible):
			self.visible = False
		else:
			self.visible = True
	
	def setColor(self, r, g, b):
		self.color = f"\033[38;2;{r};{g};{b}m"


