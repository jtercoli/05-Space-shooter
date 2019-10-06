# Space Shooter
# Jadan Ercoli 2019

import sys, logging, arcade, open_color

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Wild & Wacky Space Sh00ter"

NUM_ENEMIES = 8
STARTING_LOCATION = (400,100)
BULLET_DAMAGE = 15
ENEMY_HP = 120
HIT_SCORE = 15
KILL_SCORE = 50


class Background(arcade.Sprite):
    def __init__(self):
        super().__init__("assets/Background Stars.png")
        self.Background = Background



class Bullet(arcade.Sprite):

    #initializes the bullet
    def __init__(self, position, velocity, damage):
        super().__init__("assets/bullet.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity 
        self.damage = damage

    # moves the bullet
    def update(self):
        self.center_x += self.dx
        self.center_y += self.dy

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("assets/Scarab.png", 0.5)
        (self.center_x, self.center_y) = STARTING_LOCATION

#Creates enemy class
class Enemy(arcade.Sprite):
    #Initializes the enemy ship and location
    def __init__(self,position):
        super().__init__("assets/Louse.png", 0.5)
        self.hp = ENEMY_HP
        (self.center_x, self.center_y) = position


class Window(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)
        arcade.set_background_color(open_color.black)
        self.Background = Background
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player = Player()
        self.score = 0


    #Set up enemies 
    def setup(self):
        for i in range(NUM_ENEMIES):
            x = 120 * (i+1) + 40
            y = 500
            enemy = Enemy((x,y))
            self.enemy_list.append(enemy)

    def update(self, delta_time):
        self.bullet_list.update()
        for e in self.enemy_list:
            damage = arcade.check_for_collision_with_list(e, self.bullet_list)
            for d in damage:
                e.hp -= d.damage
                d.kill()
                if e.hp <= 0:
                    self.score += KILL_SCORE
                    e.kill()
                else:
                    self.score += HIT_SCORE

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_text(str(self.score), 20, SCREEN_HEIGHT - 40, open_color.white, 16)
        self.player.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()




    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.player.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            x = self.player.center_x
            y = self.player.center_y
            bullet = Bullet((x,y), (0,10), BULLET_DAMAGE)
            self.bullet_list.append(bullet)

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            print("Left")
        elif key == arcade.key.RIGHT:
            print("Right")
        elif key == arcade.key.UP:
            print("Up")
        elif key == arcade.key.DOWN:
            print("Down")

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        pass


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()