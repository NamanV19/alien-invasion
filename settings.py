class Settings():
 """A class to store all settings for Alien Invasion."""
 def __init__(self):
    self.screen_width = 1100
    self.screen_height = 650
    self.bg_color = (0, 255, 0)
    self.ship_speed_factor = 1.5

    self.bullet_speed_factor = 1
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = 60, 60, 60
    self.bullets_allowed = 3
