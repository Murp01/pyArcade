import time

import arcade
from arcade.examples.decorator_drawing_example import draw_pine_tree, draw_bird

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drawing With Functions Example"

#Draw background specifically sky and ground
def draw_background():
        arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      SCREEN_HEIGHT * (1/3),
                                      arcade.color.SKY_BLUE)
        arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT /3,
                                      0,
                                      arcade.color.DARK_SPRING_GREEN)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    #Start the render process.  This must be done before any drawing commands
    arcade.start_render()

    #Call our drawing functions
    draw_background()
    draw_pine_tree(350, 250)
    draw_pine_tree(350, 320)
    draw_bird(70, 500)
    draw_bird(470, 550)

    arcade.finish_render()

    arcade.run()

if __name__ == "__main__":
    main()
