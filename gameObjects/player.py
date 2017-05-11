class player:
	def __init__(self,positionX,positionY):
		self.positionX = positionX
		self.positionY = positionY

		self.width = 32
		self.height = 32
	def getPosition(self):
		return [self.positionX-(self.width/2),self.positionY-(self.height/2)]
	def setPosition(self,position):
		self.positionX = position[0]
		self.positionY = position[1]
	def getDimensions(self):
		return [self.width,self.height]
