import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Super Timberland Bros"
FULL_SCREEN = True

"""Constants used to scale sprites from original size"""
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

"""Constant for movement speed"""
PLAYER_MOVEMENT_SPEED = 5

"""Constants for gravity"""
GRAVITY = 1
PLAYER_JUMP_SPEED = 20


class MyGame(arcade.Window):
    """Call parent class and set up the window"""
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        """Set up lists"""
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        """ Separate variable that holds the player sprite """
        self.player_sprite = None

        """Add basic physics engine"""
        self.physics_engine = None

    """Set up game here.  Call function to restart the game"""
    def setup(self):
        """Create the spritelists"""
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        """Set up the player, specifically placing it at these coordinates."""
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        """Create the ground. """
        """This shows using a loop to place multiple sprites horizontally"""
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        """Put some crates on the ground.  This shows using a coordinate list to place sprites"""
        coordinate_list = [[512, 96],
                           [256, 96],
                           [768, 96]]

        for coordinate in coordinate_list:
            """Add a crate on the ground"""
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

        """Create the 'physics engine"""
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()
        """Code to draw the screen goes here"""

        """Draw the sprites"""
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed"""
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Move the player with the physics engine
        self.physics_engine.update()

def main():
    """Main method"""
    window = MyGame()
    window.setup()
    arcade.run()

"""When interpreter runs the source file it assigns main to the name variable within the module.
So this bsically checks if file is runnnig.  If so it calls the main method which runs game"""
if __name__ == "__main__":
    main()
