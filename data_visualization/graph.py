from common.scene_object import SceneObject
from data_visualization.datapoints import createDatapoints

class Graph(SceneObject):

    def __init__(self, program_reference, transformation_uniform, position_variable_name, color_variable_name):
        points = createDatapoints()
        points = sorted(points, key=lambda point: point[-1], reverse=True)
        positions = self.generate_positions(points)
        colors = self.generate_colors(points)
        super().__init__(program_reference, transformation_uniform, position_variable_name, positions, color_variable_name, colors)
    

    def generate_positions(self, points):
        positions = []
        for point in points:
            weight = point[2]
            half_length = (weight + 15) / 50

            bottom_left = [point[0] - half_length, point[1] - half_length, 0.0]
            bottom_right = [point[0] + half_length, point[1] - half_length, 0.0]
            top_left = [point[0] - half_length, point[1] + half_length, 0.0]
            top_right = [point[0] + half_length, point[1] + half_length, 0.0]

            positions.extend([bottom_left, top_right, top_left, bottom_right, top_right, bottom_left])
        return positions
    

    def generate_colors(self, points):
        colors = []
        for point in points:
            y = point[1]
            blue = max(0.0, min(y/30, 1.0))
            red = 1 - blue
            colors.append([red, 0.0, blue] * 6)
        return colors
