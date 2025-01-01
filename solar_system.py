from program import Program
import numpy as np
from OpenGL.GL import *


class SolarSystem(Program):

    PROGRAM_NAME = 'Solar System'
    VERTEX_SHADER_FILE = 'solar-system-vs.glsl'
    FRAGMENT_SHADER_FILE = 'solar-system-fs.glsl'


    def __init__(self):
        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self):
        vao_reference = glGenVertexArrays(1)
        glBindVertexArray(vao_reference)
        
        positions = [0.0, 0.8, 0.0,
                    0.8, -0.8, 0.0,
                    -0.8, -0.8, 0.0]
        
        vertex_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, np.array(positions, dtype=np.float32), GL_STATIC_DRAW)
        position_variable_reference = glGetAttribLocation(self.program, 'position')
        glVertexAttribPointer(position_variable_reference, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(position_variable_reference)


    def update_scene(self):
        glDrawArrays(GL_TRIANGLES, 0, 3)
