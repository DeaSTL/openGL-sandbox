from chunk import chunk
import numpy as np
from opensimplex import OpenSimplex
import json

class world():
	def __init__(self):
		self.chunk_array = np.empty((15,15),dtype=object)
		self.spnoise = OpenSimplex()
	def onLoad(self):
		pass
	def generateChunks(self):
		for x in range(0,15):
			for y in range(0,15):
				self.chunk_array[x][y] = chunk(x,y,self.spnoise)
				
		return self.chunk_array
	def getChunkArray(self):
		tmpChunks = []
		for chunkl in self.chunk_array:
			for chunk in chunkl:
				tmpChunks.append(chunk)
		return tmpChunks
	def saveWorld(self):
		np.save("world",self.chunk_array)
	def loadWorld(self):
		self.chunk_array = np.load("world.npy")


			
		
			

