import terrain_block
import settings


class dirt(terrain_block.block):
	def __init__(self,positionX,positionY):
		self.positionX = positionX
		self.positionY = positionY

		self.width = 32
	
		self.textureDir = settings.DEFINITIONS_ROOT+"/textures/terrain/dirt_terrain_block.png"

		self.type = "terrain_dirt"

		self.Xindex = 0
		self.Yindex = 0 
class stone(terrain_block.block):
	def __init__(self,positionX,positionY):
		self.positionX = positionX
		self.positionY = positionY
		
		self.width = 32

		self.textureDir = settings.DEFINITIONS_ROOT+"/textures/terrain/stone_terrain_block.png"
		
		self.type = "terrain_stone"

		self.Xindex = 0
		self.Yindex = 0