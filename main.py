import pyglet
from gameObjects.world import world
import numpy as np

'''

'''
window = pyglet.window.Window(500,500,resizable=True)
world = world()
world.generateChunks()
tile_array = np.empty((15,15),dtype=object)
playerSpeed = [0,0]
#world.saveWorld()
#for chunk in world.getChunkArray():
#	print(str(chunk.x)+","+str(chunk.y))
#	for block in chunk.getChunk():
#		print("|-"+str(block.positionX)+","+str(block.positionY)+"--"+str(block.getCenter()))

for block in world.getChunkArray()[0].getChunk():
		image = pyglet.image.load(block.textureDir)
		sprite = pyglet.sprite.Sprite(image,x=block.positionX*block.width,y=block.positionY*block.width)
		tile_array[block.getIndex()[0]][block.getIndex()[1]] = sprite
		print(type(sprite))
def update_map():
	for i in range(0,15):
		for j in range(0,15):
			if not tile_array[i][j] == None:
				tile_array[i][j].x+= playerSpeed[0]
				tile_array[i][j].x+= playerSpeed[1]
				tile_array[i][j].draw()
def run(value):
	update_map()
def main():
	@window.event 
	def on_draw():
		window.clear()
		run(None) 
	@window.event
	def on_key_press(sym,mod):
		playerSpeed[0] = 5
	@window.event
	def on_key_release(sym,mod):
		playerSpeed[0] = 0
	
	
	pyglet.clock.schedule_interval(run,0.03)
	pyglet.app.run()
main()


