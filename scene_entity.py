from math import cos, sin
import numpy as np

class SceneEntity(object):

    def __init__(self):
        self.model_matrix = np.identity(4, dtype=np.float32)
    

    def transform(self, matrix, locally=True):
        if locally:
            self.model_matrix = self.model_matrix @ matrix
        else:
            self.model_matrix = matrix @ self.model_matrix
    

    def translate(self, x, y, z, locally=True):
        translation_matrix = np.array([[1, 0, 0, x],
                                       [0, 1, 0, y],
                                       [0, 0, 1, z],
                                       [0, 0, 0, 1]]).astype(np.float32)
        self.transform(translation_matrix, locally)
    

    def scale(self, scale, locally=True):
        scale_matrix = np.array([[scale, 0, 0, 0],
                                 [0, scale, 0, 0],
                                 [0, 0, scale, 0],
                                 [0, 0, 0, 1]]).astype(np.float32)
        self.transform(scale_matrix, locally)
    

    def rotate_around_x(self, angle, locally=True):
        rotation_matrix = np.array([[1, 0,  0, 0],
                                    [0, cos(angle), -sin(angle), 0],
                                    [0, sin(angle),  cos(angle), 0],
                                    [0, 0,  0, 1]]).astype(np.float32)
        self.transform(rotation_matrix, locally)


    def rotate_around_y(self, angle, locally=True):
        rotation_matrix = np.array([[cos(angle), 0, sin(angle), 0],
                                    [0, 1, 0, 0],
                                    [-sin(angle), 0, cos(angle), 0],
                                    [0, 0, 0, 1]]).astype(np.float32)
        self.transform(rotation_matrix, locally)
    

    def rotate_around_z(self, angle, locally=True):
        rotation_matrix = np.array([[cos(angle), -sin(angle), 0, 0],
                                    [sin(angle), cos(angle), 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]]).astype(np.float32)
        self.transform(rotation_matrix, locally)
