from ev3dev2simulator.config.config import get_simulation_settings
from ev3dev2simulator.robotpart.BodyPart import BodyPart


class Brick(BodyPart):
    """
    Class representing the body of the simulated robotpart.
    """

    def __init__(self, config, robot):
        dims = get_simulation_settings()['body_part_sizes']['body']
        super().__init__(config, robot, int(dims['width']), int(dims['height']), 'brick')

    def setup_visuals(self, scale):
        vis_conf = get_simulation_settings()
        self.init_sprite(vis_conf['image_paths']['body'], scale)
