class Tri:
	def __init__(self):
		self.l1 = None
		self.l2 = None
		self.l3 = None
		self.depth = 0
		self.color = "\033[38;2;255;0m"
		self.type = "triangle"
		self.visible = True
	def setEdges(self, x, y, z):
		if(x.v2 == y.v1 and y.v2 == z.v1 and z.v2 == x.v1):
			self.l1 = x
			self.l2 = y
			self.l3 = z
		else:
			raise("non closed triangle")
	def setColor(self, r, g, b):
		self.color = f"\033[38;2;{r};{g};{b}m"


