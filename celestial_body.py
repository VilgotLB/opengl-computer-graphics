from scene_object import SceneObject
from sphere import generateSphere

class CelestialBody(SceneObject):

    def __init__(self, program_reference, model_matrix_uniform, position_variable_name, color_variable_name, base_color):
        positions = generateSphere()
        colors = base_color * len(positions)
        super().__init__(program_reference, model_matrix_uniform, position_variable_name, positions, color_variable_name, colors)
