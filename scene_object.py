import numpy as np
from OpenGL.GL import *
from matrix import Matrix

class SceneObject(object):

    def __init__(self, program_reference, position_variable_name, positions):
        self.positions = np.array(positions).ravel().astype(np.float32)
        self.number_of_triangles = len(self.positions) // 3

        vertex_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, self.positions, GL_STATIC_DRAW)
        position_variable_reference = glGetAttribLocation(program_reference, position_variable_name)
        glVertexAttribPointer(position_variable_reference, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(position_variable_reference)
    

    def render(self):
        glDrawArrays(GL_TRIANGLES, 0, self.number_of_triangles)
