import pyglet


window = pyglet.window.Window(500, 500, resizable=True)
batch = pyglet.graphics.Batch()

pyglet.resource.path.append("textures/terrain")
pyglet.resource.reindex()

background_tiles = []
scrolling = [0, 0]


def populate_map():
    image = pyglet.resource.image("default_terrain_block.png")
    for x in range(15):
        x *= image.width
        for y in range(15):
            y *= image.height
            block_spr = pyglet.sprite.Sprite(img=image, x=x, y=y, batch=batch)
            background_tiles.append(block_spr)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(key, mod):
    global scrolling
    if key == pyglet.window.key.D:
        scrolling[0] += 5
    elif key == pyglet.window.key.A:
        scrolling[0] -= 5
    if key == pyglet.window.key.W:
        scrolling[1] += 5
    elif key == pyglet.window.key.S:
        scrolling[1] -= 5


@window.event
def on_key_release(key, mod):
    global scrolling
    if key == pyglet.window.key.D or key == pyglet.window.key.A:
        scrolling[0] = 0
    if key == pyglet.window.key.W or key == pyglet.window.key.S:
        scrolling[1] = 0


def update(dt):
    global scrolling
    x, y = scrolling
    pyglet.gl.glTranslatef(x, y, 0)         # OpenGL command move the "camera"


if __name__ == "__main__":
    populate_map()
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()





