import arcade
import time

#Constants for scene size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#Open window set window title and dimensions (w,h)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

#Set background colour to white (alpha etc and be set
arcade.set_background_color(arcade.color.WHITE)

#Start render process.  Must be done before drawing commands
arcade.start_render()

#Draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

#Draw right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

#Draw left eye
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

#Draw the smile
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

#Finish drawing and display the result
arcade.finish_render()

#Keep window open until user hits the 'close' button
arcade.run()



