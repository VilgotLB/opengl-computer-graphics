from math import cos, sin
import numpy as np

class SceneEntity(object):

    def __init__(self):
        self.model_matrix = np.identity(4, dtype=np.float32)
    

    def translate(self, x, y, z):
        translation_matrix = np.array([[1, 0, 0, x],
                                       [0, 1, 0, y],
                                       [0, 0, 1, z],
                                       [0, 0, 0, 1]]).astype(np.float32)
        self.model_matrix = translation_matrix @ self.model_matrix
    

    def scale(self, scale):
        scale_matrix = np.array([[scale, 0, 0, 0],
                                 [0, scale, 0, 0],
                                 [0, 0, scale, 0],
                                 [0, 0, 0, 1]]).astype(np.float32)
        self.model_matrix = scale_matrix @ self.model_matrix
    

    def rotate_around_x(self, angle):
        rotation_matrix = np.array([[1, 0,  0, 0],
                                    [0, cos(angle), -sin(angle), 0],
                                    [0, sin(angle),  cos(angle), 0],
                                    [0, 0,  0, 1]]).astype(np.float32)
        self.model_matrix = rotation_matrix @ self.model_matrix


    def rotate_around_y(self, angle):
        rotation_matrix = np.array([[cos(angle), 0, sin(angle), 0],
                                    [0, 1, 0, 0],
                                    [-sin(angle), 0, cos(angle), 0],
                                    [0, 0, 0, 1]]).astype(np.float32)
        self.model_matrix = rotation_matrix @ self.model_matrix
    

    def rotate_around_z(self, angle):
        rotation_matrix = np.array([[cos(angle), -sin(angle), 0, 0],
                                    [sin(angle), cos(angle), 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]]).astype(np.float32)
        self.model_matrix = rotation_matrix @ self.model_matrix
