import numpy as np
from OpenGL.GL import *
from matrix import Matrix

class SceneObject(object):

    def __init__(self, program_reference, position_variable_name, positions, color_variable_name, colors):
        self.number_of_vertices = len(positions)

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.store_vertex_attribute(program_reference, position_variable_name, positions)
        self.store_vertex_attribute(program_reference, color_variable_name, colors)

        self.model_matrix = Matrix.makeIdentity()
        self.modelMatrix_reference = glGetUniformLocation(program_reference, 'modelMatrix')
    

    def store_vertex_attribute(self, program, variable_name, data):
        data = np.array(data).ravel().astype(np.float32)

        vertex_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, data, GL_STATIC_DRAW)

        variable_reference = glGetAttribLocation(program, variable_name)
        glVertexAttribPointer(variable_reference, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(variable_reference)
    

    def translate(self, x, y, z):
        self.model_matrix = Matrix.makeTranslation(x, y, z) @ self.model_matrix
    

    def scale(self, scale):
        self.model_matrix = Matrix.makeScale(scale) @ self.model_matrix
    

    def rotate_around_x(self, angle):
        self.model_matrix = Matrix.makeRotationX(angle) @ self.model_matrix


    def rotate_around_y(self, angle):
        self.model_matrix = Matrix.makeRotationY(angle) @ self.model_matrix
    

    def rotate_around_z(self, angle):
        self.model_matrix = Matrix.makeRotationZ(angle) @ self.model_matrix


    def render(self):
        glBindVertexArray(self.vao)

        glUniformMatrix4fv(self.modelMatrix_reference, 1, GL_TRUE, self.model_matrix)

        glDrawArrays(GL_TRIANGLES, 0, self.number_of_vertices)
