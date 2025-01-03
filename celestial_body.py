from scene_object import SceneObject
from sphere import generateSphere
from math import sin, pi

class CelestialBody(SceneObject):

    def __init__(self, program_reference, model_matrix_uniform, position_variable_name, color_variable_name, base_color):
        positions = generateSphere()
        colors = self.generate_colors(positions, base_color)
        super().__init__(program_reference, model_matrix_uniform, position_variable_name, positions, color_variable_name, colors)


    def generate_colors(self, positions, base_color):
        colors = []
        for position in positions:
            color = []
            for i in range(3):
                variation = sin(position[i] * pi * 4) * 0.2
                channel_value = base_color[i] + variation
                channel_value = max(min(channel_value, 1.0), 0.0)
                color.append(channel_value)
            colors.append(color)
        return colors
