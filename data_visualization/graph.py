from common.scene_object import SceneObject
from data_visualization.datapoints import createDatapoints
import random

class Graph(SceneObject):
    """Represents a graph for visualizing datapoints."""

    def __init__(self, program_reference: int, transformation_uniform: str, position_variable_name: str, center_variable_name: str, color_variable_name: str):
        """Initialize the Graph with vertex data and shader program references."""

        # Generate and sort datapoints by their weight (largest to smallest, to reduce the risk of large datapoints covering smaller ones during rendering)
        points = createDatapoints()
        points = sorted(points, key=lambda point: point[-1], reverse=True)

        # Generate vertex positions, center positions, and colors
        positions, centers = self.generate_positions(points)
        colors = self.generate_colors(points)

        # Initialize the parent SceneObject with these vertex positions and colors.
        super().__init__(program_reference, transformation_uniform, position_variable_name, positions, color_variable_name, colors)

        # Store the centers as an additional vertex attribute.
        self.store_vertex_attribute(self.program, center_variable_name, centers)
    

    def generate_positions(self, points: list[list[float]]) -> tuple[list[list[float], list[list[float]]]]:
        """Generate vertex positions and center positions for the graph's datapoints."""

        positions = []
        centers = []
        for point in points:
            # Weight determines the quad's size
            weight = point[2]
            half_length = (weight + 15) / 50

            # Define the four corners of the quad and the center position
            bottom_left = [point[0] - half_length, point[1] - half_length, 0.0]
            bottom_right = [point[0] + half_length, point[1] - half_length, 0.0]
            top_left = [point[0] - half_length, point[1] + half_length, 0.0]
            top_right = [point[0] + half_length, point[1] + half_length, 0.0]
            center = [point[0], point[1], 0.0]

            # Add two triangles to form the quad, and add the center positions for each vertex. 
            positions.extend([bottom_left, top_right, top_left, bottom_right, top_right, bottom_left])
            centers.extend([center]*6)

        return positions, centers
    

    def generate_colors(self, points: list[list[float]]) -> list[list[float]]:
        """Generate vertex colors for the graph's datapoints."""

        colors = []
        for point in points:
            y = point[1]                        # Use y-coordinate to determine color
            blue = max(0.0, min(y/30, 1.0))     # Normalize y to range [0, 1]
            red = 1 - blue                      # Red decreases as blue increases
            green = random.uniform(0.0, 0.5)    # Random green component for variety

            # Repeat the color for all six vertices of the quad
            colors.append([red, green, blue] * 6)
        return colors
