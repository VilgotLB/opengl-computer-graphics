from common.program import Program
from data_visualization.graph import Graph

class DataVisualization(Program):

    PROGRAM_NAME = 'Data Visualization'
    VERTEX_SHADER_FILE = 'data_visualization/data-vis-vs.glsl'
    FRAGMENT_SHADER_FILE = 'data_visualization/data-vis-fs.glsl'
    TRANSFORMATION_UNIFORM = 'graphTransformation'
    POSITION_VARIABLE = 'position'
    COLOR_VARIABLE = 'vertexColor'

    def __init__(self):
        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self):
        self.graph = Graph(self.program, self.TRANSFORMATION_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE)
        self.graph.scale(1/50)
        self.graph.translate(-20, -20, 0)


    def update_scene(self, dt, time):
        self.graph.render()
