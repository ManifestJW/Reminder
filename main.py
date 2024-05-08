import pyglet

SCRN_W = 200
SCRN_H = 200

ASPR_W = 1
ASPR_H = 1

gWindow = pyglet.window.Window(SCRN_W, SCRN_H, "Remind")

gWindow.minimize()

boom = pyglet.media.load('assets/Sounds/vineboom.mp3')

player = pyglet.media.Player()

for x in range(5):
    player.queue(boom)

player.play()

@gWindow.event
def on_draw():
    gWindow.clear()

@player.event
def on_player_eos():
    pyglet.app.exit()

pyglet.app.run()