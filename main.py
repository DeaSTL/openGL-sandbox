import pyglet
from gameObjects.world import world
import numpy as np

from pyglet.window import key

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
		if not block == None:
			image = pyglet.image.load(block.textureDir)
			sprite = pyglet.sprite.Sprite(image,x=block.positionX*block.width,y=block.positionY*block.width)
			tile_array[(block.positionX%15)-1][(block.positionY%15)-1] = sprite
			print(len(tile_array))
def update_map():
	for i in range(0,15):
		for j in range(0,15):
			if not tile_array[i][j] == None:
				tile_array[i][j].x+= playerSpeed[0]
				tile_array[i][j].y+= playerSpeed[1]
				tile_array[i][j].draw()
def run(value):
	update_map()
def main():
	keys = key.KeyStateHandler()
	window.push_handlers(keys)
	@window.event 
	def on_draw():
		window.clear()
		run(None) 
	@window.event
	def on_key_press(sym,mod):
		if sym == 97: playerSpeed[0] = -5
		if sym == 100: playerSpeed[0] = 5
		if sym == 115: playerSpeed[1] = -5
		if sym == 119: playerSpeed[1] = 5
	@window.event
	def on_key_release(sym,mod):
		playerSpeed[0] = 0
		playerSpeed[1] = 0
	
	
	pyglet.clock.schedule_interval(run,0.03)
	pyglet.app.run()
main()


