class block(object):
	def __init__(self,positionX,positionY):
		self.positionX = positionX
		self.positionY = positionY
		self.width = 32

		self.textureDir = "textures/terrain/default_terain_block.png"

		self.type = "terrain_default"

		self.Xindex = 0
		self.Yindex = 0 
	def initialization(self):
		pass
	def getX(self): #XDDDDDDDDDDDDDDDDDDDD
		return self.positionX
	def getY(self):
		return self.positionY
	def getTexture(self):
		return self.textureDir
	def getCenter(self):
		return (self.positionX+(self.width/2),self.positionY+(self.width/2))
	def getIndex(self):
		return [self.Xindex,self.Yindex]
