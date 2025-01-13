from OpenGL.GL import *
from common.scene_object import SceneObject
from solar_system.sphere import generateSphere
from math import sin, pi

class CelestialBody(SceneObject):
    """Represents a spherical celestial body in a solar system, such as a planet or the sun."""

    def __init__(self, program_reference: int, model_matrix_uniform: str, glossiness_uniform: str, is_sun_uniform: str, position_variable_name: str, color_variable_name: str, base_color: list[float], glossiness: float, is_sun: bool = False):
        """Initialize a CelestialBody with vertex data, shader references, and physical properties."""

        # Generate position and color attributes, and initialize the parent SceneObject with these attributes.
        positions = generateSphere()
        colors = self.generate_colors(positions, base_color)
        super().__init__(program_reference, model_matrix_uniform, position_variable_name, positions, color_variable_name, colors)

        # Store the shader uniform references for glossiness and whether the celestial body is the sun.
        self.is_sun_reference = glGetUniformLocation(self.program, is_sun_uniform)
        self.is_sun = is_sun
        self.glossiness_reference = glGetUniformLocation(self.program, glossiness_uniform)
        self.glossiness = glossiness


    def generate_colors(self, positions: list[list[float]], base_color: list[float]) -> list[list[float]]:
        """Generate varied vertex colors based on the base color."""

        colors = []
        for position in positions:
            color = []
            for i in range(3):
                # Create color variation using the sine function with the sphere's coordinates as input.
                variation = sin(position[i] * pi * 4) * 0.4
                channel_value = base_color[i] + variation
                channel_value = max(min(channel_value, 1.0), 0.0)   # Between 0 and 1.
                color.append(channel_value)
            colors.append(color)
        return colors
    

    def render(self) -> None:
        """Render the celestial body."""

        # Update the 'is_sun' and 'glossiness' uniforms in the shader with this CelestialBody's data before rendering
        glUniform1i(self.is_sun_reference, self.is_sun)
        glUniform1f(self.glossiness_reference, self.glossiness)
        super().render()
