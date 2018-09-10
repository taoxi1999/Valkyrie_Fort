import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


arcade.open_window(600,600,"Exp")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for x in range(0, 601, 120):
    arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 2)

for y in range(0, 601, 200):
    arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 2)

arcade.finish_render()

arcade.run()
