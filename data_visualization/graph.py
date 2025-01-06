from common.scene_object import SceneObject

class Graph(SceneObject):

    def __init__(self, program_reference, transformation_uniform, position_variable_name, color_variable_name, points):
        positions = self.generate_positions(points)
        colors = self.generate_colors(points)
        super().__init__(program_reference, transformation_uniform, position_variable_name, positions, color_variable_name, colors)
    

    def generate_positions(self, points):
        positions = []
        for point in points:
            half_length = 1.0
            bottom_left = [point[0] - half_length, point[1] - half_length, 0.0]
            bottom_right = [point[0] + half_length, point[1] - half_length, 0.0]
            top_left = [point[0] - half_length, point[1] + half_length, 0.0]
            top_right = [point[0] + half_length, point[1] + half_length, 0.0]
            positions.extend([bottom_left, top_right, top_left, bottom_right, top_right, bottom_left])
        return positions
    

    def generate_colors(self, points):
        colors = []
        for point in points:
            colors.append([1.0, 1.0, 0.0] * 6)
        return colors
