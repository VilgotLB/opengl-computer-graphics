from scene_entity import SceneEntity
from OpenGL.GL import *
import numpy as np
from math import tan, pi

class Camera(SceneEntity):

    def __init__(self, program_reference, projection_view_matrix_uniform):
        super().__init__()
        self.projectionViewMatrix_reference = glGetUniformLocation(program_reference, projection_view_matrix_uniform)
    

    def get_view_matrix(self):
        return np.linalg.inv(self.model_matrix)
    

    def get_projection_matrix(self, angle_of_view=60, aspect_ratio=1, near=0.1, far=1000):
        a = angle_of_view * pi / 180.0
        d = 1.0 / tan(a / 2)
        r = aspect_ratio
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)
        return np.array([[d/r, 0, 0, 0],
                         [0, d, 0, 0],
                         [0, 0, b, c],
                         [0, 0, -1, 0]]).astype(np.float32)
    

    def activate(self):
        projection_view_matrix = self.get_projection_matrix() @ self.get_view_matrix()
        glUniformMatrix4fv(self.projectionViewMatrix_reference, 1, GL_TRUE, projection_view_matrix)
