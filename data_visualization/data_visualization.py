from common.program import Program
from data_visualization.graph import Graph
from common.scene_object import SceneObject
from OpenGL.GL import *

class DataVisualization(Program):
    """The data visualization program."""

    # Shader program and variable configuration
    PROGRAM_NAME = 'Data Visualization'
    VERTEX_SHADER_FILE = 'data_visualization/data-vis-vs.glsl'
    FRAGMENT_SHADER_FILE = 'data_visualization/data-vis-fs.glsl'
    TRANSFORMATION_UNIFORM = 'transformation'
    POSITION_VARIABLE = 'position'
    CENTER_VARIABLE = 'centerPos'
    COLOR_VARIABLE = 'vertexColor'

    def __init__(self):
        """Initialize the DataVisualization program."""

        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self) -> None:
        """Set up the data visualization scene."""

        # Create the graph, and transform it so it spans coordinates (-20, -20) to (60, 60)
        self.graph = Graph(self.program, self.TRANSFORMATION_UNIFORM, self.POSITION_VARIABLE, self.CENTER_VARIABLE, self.COLOR_VARIABLE)
        self.graph.scale(1/40)
        self.graph.translate(-20, -20, 0)

        # Enable blending for transparency effects
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    def update_scene(self, dt: float, time: float) -> None:
        """Update the data visualization scene."""
        
        self.graph.render()
