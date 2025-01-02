from matrix import Matrix

class SceneEntity(object):

    def __init__(self):
        self.model_matrix = Matrix.makeIdentity()
    

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
