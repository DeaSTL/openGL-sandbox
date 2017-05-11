import terrain.blocks as blocks
import numpy as np

class chunk():
	def __init__(self,x,y,spnoise):
		self.x = x
		self.y = y 
		self.objectList = np.empty((15,15),dtype=object)
		self.unit_width = 32
		self.total_width = self.unit_width*16
		for i in range(0,15):
			for j in range(0,15):
				y = spnoise.noise2d(x=i,y=j)*1000
				
				if y>2:
					self.objectList[i][j] = blocks.dirt(i+1*self.unit_width*self.x,j+1*self.unit_width*self.y)
					self.objectList[i][j].Xindex=i
					self.objectList[i][j].Xindex=j
				else:
					self.objectList[i][j] = blocks.stone(i+1*self.unit_width*self.x,j+1*self.unit_width*self.y)
					self.objectList[i][j].Xindex=i
					self.objectList[i][j].Xindex=j
	def getChunk(self):
		tmpBlocks = []
		for blockl in self.objectList:
			for block in blockl:
				tmpBlocks.append(block)
		return tmpBlocks
