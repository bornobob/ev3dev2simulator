from ev3dev2simulator.config.config import get_simulation_settings
from ev3dev2simulator.robotpart.BodyPart import BodyPart

COLORS = dict()
COLORS[0] = 0  # set black for no color
COLORS[1] = 0
COLORS[2] = 1
COLORS[3] = 2
COLORS[4] = 5
COLORS[5] = 3
COLORS[6] = 4


class ColorSensor(BodyPart):
    """
    Class representing a ColorSensor of the simulated robotpart.
    """

    def __init__(self, config, robot):
        dims = get_simulation_settings()['body_part_sizes']['color_sensor']
        super().__init__(config, robot, int(dims['width']), int(dims['height']), 'color_sensor', driver_name='lego-ev3-color')
        self.old_texture_index = 0

    def setup_visuals(self, scale):
        img_cfg = get_simulation_settings()['image_paths']
        src_list = [img_cfg[f'color_sensor_{color}'] for color in ['black', 'blue', 'green', 'red', 'white', 'yellow']]
        self.init_sprite_with_list(src_list, scale)

    def get_latest_value(self):
        latest_data = self.get_sensed_color()
        self.set_color_texture(latest_data)
        return latest_data

    def get_sensed_color(self) -> int:
        """
        Get the color this ColorSensor is currently 'seeing'.
        :return: integer value representing the color.
        """

        for o in self.sensible_obstacles:
            if o.collided_with(self.sprite.center_x, self.sprite.center_y):
                return o.color_code

        return self.get_default_value()

    def get_default_value(self):
        """
        1 is the color of black for the real robotpart. Playing field surface is black.
        :return: integer value representing the color black.
        """
        return 0

    def set_color_texture(self, color):
        converted = COLORS[color]
        if self.old_texture_index != converted:
            self.old_texture_index = converted
            self.sprite.set_texture(converted)
