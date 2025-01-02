from scene_entity import SceneEntity
from matrix import Matrix
from OpenGL.GL import *
import numpy as np

class Camera(SceneEntity):

    def __init__(self, program_reference, projection_view_matrix_uniform):
        super().__init__()
        self.projectionViewMatrix_reference = glGetUniformLocation(program_reference, projection_view_matrix_uniform)
    

    def get_view_matrix(self):
        return np.linalg.inv(self.model_matrix)
    

    def get_projection_matrix(self):
        return Matrix.makePerspective()
    

    def activate(self):
        projection_view_matrix = self.get_projection_matrix() @ self.get_view_matrix()
        glUniformMatrix4fv(self.projectionViewMatrix_reference, 1, GL_TRUE, projection_view_matrix)
