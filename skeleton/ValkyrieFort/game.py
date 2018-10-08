import arcade
import classes



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


window = arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'exp')
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
#setup testing grids
for x in range(0, 800, 10):
    arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 2)

for y in range(0, 800, 10):
    arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 2)



arcade.finish_render()

arcade.run()
