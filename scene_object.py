import numpy as np
from OpenGL.GL import *
from matrix import Matrix

class SceneObject(object):

    def __init__(self, program_reference, position_variable_name, positions):
        self.program = program_reference
        self.positions = np.array(positions).ravel().astype(np.float32)
        self.number_of_vertices = len(self.positions) // 3

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        vertex_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, self.positions, GL_STATIC_DRAW)
        position_variable_reference = glGetAttribLocation(self.program, position_variable_name)
        glVertexAttribPointer(position_variable_reference, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(position_variable_reference)

        self.model_matrix = Matrix.makeIdentity()
        self.modelMatrix_reference = glGetUniformLocation(self.program, 'modelMatrix')
    

    def translate(self, x, y, z):
        self.model_matrix = Matrix.makeTranslation(x, y, z) @ self.model_matrix


    def render(self):
        glBindVertexArray(self.vao)

        glUniformMatrix4fv(self.modelMatrix_reference, 1, GL_TRUE, self.model_matrix)

        glDrawArrays(GL_TRIANGLES, 0, self.number_of_vertices)
