import pyglet

'''

'''
window = pyglet.window.Window(500,500,resizable=True)
def run(value):
	pass
def main():
	@window.event
	def on_draw():
		window.clear()
		run(None)
	pyglet.clock.schedule_interval(run,0.03)
	pyglet.app.run()
main()


