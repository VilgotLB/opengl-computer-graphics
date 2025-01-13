from math import cos, sin
import numpy as np

class SceneEntity(object):
    """Represents an entity in an OpenGL scene within a scene graph."""

    def __init__(self):
        """Initialize the SceneEntity with an identity model matrix and no parent or children."""

        self.model_matrix = np.identity(4, dtype=np.float32)
        self.parent = None
        self.children = []
    

    def add_child(self, child: 'SceneEntity') -> None:
        """Add a child to this entity."""

        child.parent = self
        self.children.append(child)
    

    def remove_child(self, child: 'SceneEntity') -> None:
        """Remove a child from this entity."""

        child.parent = None
        self.children.remove(child)
    

    def get_world_matrix(self) -> np.ndarray:
        """Compute the world transformation matrix for this entity."""

        # Recursively apply all ancestors' transformations to get the world transformation for this entity.
        if self.parent == None:
            return self.model_matrix
        return self.parent.get_world_matrix() @ self.model_matrix
    

    def get_world_position(self) -> list[float]:
        """Get the world position of this entity."""

        # Extract the translation components of the entity's world matrix.
        world_matrix = self.get_world_matrix()
        x = world_matrix[0][3]
        y = world_matrix[1][3]
        z = world_matrix[2][3]
        return [x, y, z]
    

    def transform(self, matrix: np.ndarray, locally: bool = True) -> None:
        """Apply a transformation matrix to this entity, either locally or globally."""

        if locally:
            self.model_matrix = self.model_matrix @ matrix
        else:
            self.model_matrix = matrix @ self.model_matrix
    

    def translate(self, x: float, y: float, z: float, locally: bool = True) -> None:
        """Apply a translation to this entity."""

        translation_matrix = np.array([[1, 0, 0, x],
                                       [0, 1, 0, y],
                                       [0, 0, 1, z],
                                       [0, 0, 0, 1]]).astype(np.float32)
        self.transform(translation_matrix, locally)
    

    def scale(self, scale: float, locally: bool = True) -> None:
        """Apply a uniform scaling transformation to this entity."""

        scale_matrix = np.array([[scale, 0, 0, 0],
                                 [0, scale, 0, 0],
                                 [0, 0, scale, 0],
                                 [0, 0, 0, 1]]).astype(np.float32)
        self.transform(scale_matrix, locally)
    

    def rotate_around_x(self, angle: float, locally: bool = True) -> None:
        """Apply a rotation around the X-axis."""

        rotation_matrix = np.array([[1, 0,  0, 0],
                                    [0, cos(angle), -sin(angle), 0],
                                    [0, sin(angle),  cos(angle), 0],
                                    [0, 0,  0, 1]]).astype(np.float32)
        self.transform(rotation_matrix, locally)


    def rotate_around_y(self, angle: float, locally: bool = True) -> None:
        """Apply a rotation around the Y-axis."""

        rotation_matrix = np.array([[cos(angle), 0, sin(angle), 0],
                                    [0, 1, 0, 0],
                                    [-sin(angle), 0, cos(angle), 0],
                                    [0, 0, 0, 1]]).astype(np.float32)
        self.transform(rotation_matrix, locally)
    

    def rotate_around_z(self, angle: float, locally: bool = True) -> None:
        """Apply a rotation around the Z-axis."""
        
        rotation_matrix = np.array([[cos(angle), -sin(angle), 0, 0],
                                    [sin(angle), cos(angle), 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]]).astype(np.float32)
        self.transform(rotation_matrix, locally)
