from Funcs import utils
from Setup import Setup

plane = Setup.plane
screensize = Setup.screensize
yshrink = Setup.yshrink
visible = utils.visible
class Vertex:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.visible = True
		self.sx = None
		self.sy = None
		self.sz = None

		self.px = None
		self.py = None
		self.pz = None

		self.psx = None
		self.psy = None
		self.psz = None
		
		self.depth = 0

		self.color = "\033[38;2;0;0;255m"

		self.type = "vertex"

		if(not utils.visible(x,y)):
			self.visible = False
		else:
			self.psx = self.sx
			self.psy = self.sy
			self.psz = 0
			self.sx = int(utils.map(x,plane["nx"], plane["px"], 0, screensize["x"]))
			self.sy = int(utils.map(y*yshrink,plane["py"], plane["ny"], 0, screensize["y"]))
			self.sz = 0

	def setColor(self, r, g, b):
		self.color = f"\033[38;2;{r};{g};{b}m"

	def setX(self,x):
		self.px = self.x
		self.x = x
	
	def setY(self,y):
		self.py = self.y
		self.y = y
	
	def setZ(self,z):
		self.pz = self.z
		self.z = z
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def getZ(self):
		return self.z

	def updateSelf(self):
		if(not visible(self.x, self.y)):
			self.visible = False
		else:
			self.psx = self.sx
			self.psy = self.sy
			self.psz = 0
			self.visible = True
			self.sx = int( map(self.x, plane["nx"], plane["px"], 0, screensize["x"]))
			self.sy = int(map(self.y*yshrink, plane["py"], plane["ny"], 0, screensize["y"]))
			self.sz = 0



