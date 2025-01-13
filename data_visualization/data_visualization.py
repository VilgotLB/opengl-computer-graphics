from common.program import Program
from data_visualization.graph import Graph
from common.scene_object import SceneObject

class DataVisualization(Program):

    PROGRAM_NAME = 'Data Visualization'
    VERTEX_SHADER_FILE = 'data_visualization/test-vs.glsl'
    FRAGMENT_SHADER_FILE = 'data_visualization/test-fs.glsl'
    TRANSFORMATION_UNIFORM = 'transformation'
    POSITION_VARIABLE = 'position'
    CENTER_VARIABLE = 'centerPos'
    COLOR_VARIABLE = 'vertexColor'

    def __init__(self):
        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self):
        positions = [[-0.8, -0.8, 0.0], [0.8, -0.8, 0.0], [-0.8, 0.8, 0.0], [0.8, -0.8, 0.0], [0.8, 0.8, 0.0], [-0.8, 0.8, 0.0]]
        colors = [[1.0, 1.0, 0.0]]*6
        self.shape = SceneObject(self.program, self.TRANSFORMATION_UNIFORM, self.POSITION_VARIABLE, positions, self.COLOR_VARIABLE, colors)
        self.shape.store_vertex_attribute(self.program, self.CENTER_VARIABLE, [[0.0, 0.0, 0.0]]*6)

        self.shape.scale(1/10)
        self.shape.translate(1, 2, 0)


    def update_scene(self, dt, time):
        self.shape.render()
