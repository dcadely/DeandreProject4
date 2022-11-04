import arcade


arcade.open_window(2000,1500,"Graph paper")
my_text = arcade.Text("Population of the largest pop Nations on Earth",
700, 1300, arcade.color.AERO_BLUE,
20, font_name='Noto Sans' )
arcade.set_background_color(arcade.color.AMAZON)
WIDTH = 100
YSTART = 100
xpos = 0
arcade.start_render()
for size in range(500,1000,100):
    arcade.draw_xywh_rectangle_filled(xpos, YSTART, WIDTH, size, arcade.color.BLUE)
    xpos += 200

arcade.draw_line(500,100,1000,1000,arcade.color.BLUE,50)

my_text.draw()

arcade.finish_render()

arcade.run()
