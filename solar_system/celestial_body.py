from OpenGL.GL import *
from common.scene_object import SceneObject
from solar_system.sphere import generateSphere
from math import sin, pi

class CelestialBody(SceneObject):

    def __init__(self, program_reference, model_matrix_uniform, glossiness_uniform, is_sun_uniform, position_variable_name, color_variable_name, base_color, glossiness, is_sun=False):
        positions = generateSphere()
        colors = self.generate_colors(positions, base_color)

        super().__init__(program_reference, model_matrix_uniform, position_variable_name, positions, color_variable_name, colors)

        self.is_sun_reference = glGetUniformLocation(self.program, is_sun_uniform)
        self.is_sun = is_sun

        self.glossiness_reference = glGetUniformLocation(self.program, glossiness_uniform)
        self.glossiness = glossiness


    def generate_colors(self, positions, base_color):
        colors = []
        for position in positions:
            color = []
            for i in range(3):
                variation = sin(position[i] * pi * 4) * 0.4
                channel_value = base_color[i] + variation
                channel_value = max(min(channel_value, 1.0), 0.0)
                color.append(channel_value)
            colors.append(color)
        return colors
    

    def render(self):
        glUniform1i(self.is_sun_reference, self.is_sun)
        glUniform1f(self.glossiness_reference, self.glossiness)
        super().render()
