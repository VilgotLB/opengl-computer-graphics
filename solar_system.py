from program import Program
import numpy as np
from OpenGL.GL import *
from matrix import Matrix
from sphere import generateSphere


class SolarSystem(Program):

    PROGRAM_NAME = 'Solar System'
    VERTEX_SHADER_FILE = 'solar-system-vs.glsl'
    FRAGMENT_SHADER_FILE = 'solar-system-fs.glsl'


    def __init__(self):
        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self):
        vao_reference = glGenVertexArrays(1)
        glBindVertexArray(vao_reference)
        
        positions = generateSphere()
        self.draw_count = len(positions)
        positions = np.array(positions).ravel().astype(np.float32)
        
        vertex_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)
        position_variable_reference = glGetAttribLocation(self.program, 'position')
        glVertexAttribPointer(position_variable_reference, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(position_variable_reference)

        projection_matrix = Matrix.makePerspective()
        view_matrix = Matrix.makeTranslation(0,0,-10)
        projection_view_matrix = projection_matrix @ view_matrix

        projectionViewMatrix_reference = glGetUniformLocation(self.program, 'projectionViewMatrix')
        glUniformMatrix4fv(projectionViewMatrix_reference, 1, GL_TRUE, projection_view_matrix)


    def update_scene(self):
        glDrawArrays(GL_TRIANGLES, 0, self.draw_count)
