from common.program import Program

class DataVisualization(Program):

    PROGRAM_NAME = 'Data Visualization'
    VERTEX_SHADER_FILE = 'data_visualization/data-vis-vs.glsl'
    FRAGMENT_SHADER_FILE = 'data_visualization/data-vis-fs.glsl'


    def __init__(self):
        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self):
        pass


    def update_scene(self, dt, time):
        pass
