import terrain.blocks as blocks
import numpy as np
class chunk():
	def __init__(self,x,y,spnoise):
		self.objectList = np.empty((15,15),dtype=object)
		for i in range(0,15):
			for j in range(0,15):
				y = spnoise.noise2d(x=i,y=j)*1000
				
				if y>2:
					self.objectList[i][j] = blocks.dirt(i,j)
				else:
					self.objectList[i][j] = blocks.stone(i,j)
	def getChunk(self):
		return self.objectList