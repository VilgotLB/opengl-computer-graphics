from common.program import Program
from data_visualization.graph import Graph
from common.scene_object import SceneObject

class DataVisualization(Program):

    PROGRAM_NAME = 'Data Visualization'
    VERTEX_SHADER_FILE = 'data_visualization/test-vs.glsl'
    FRAGMENT_SHADER_FILE = 'data_visualization/test-fs.glsl'
    TRANSFORMATION_UNIFORM = 'transformation'
    POSITION_VARIABLE = 'position'
    COLOR_VARIABLE = 'vertexColor'

    def __init__(self):
        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self):
        positions = [[-0.8, -0.8, 0.0], [0.8, -0.8, 0.0], [0.8, 0.8, 0.0], [-0.8, 0.8, 0.0]]
        colors = [[1.0, 1.0, 0.0]]*4
        self.shape = SceneObject(self.program, self.TRANSFORMATION_UNIFORM, self.POSITION_VARIABLE, positions, self.COLOR_VARIABLE, colors)


    def update_scene(self, dt, time):
        self.shape.render()
