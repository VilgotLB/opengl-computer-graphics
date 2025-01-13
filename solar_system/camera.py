from common.scene_entity import SceneEntity
from OpenGL.GL import *
import numpy as np
from math import tan, pi

class Camera(SceneEntity):
    """Represents a camera in an OpenGL scene."""

    def __init__(self, program_reference: int, projection_view_matrix_uniform: str, camera_position_uniform: str):
        """Initialize the Camera with shader program references for uniforms."""

        super().__init__()

        # Get uniform locations for the projection-view matrix and camera position
        self.projection_view_matrix_reference = glGetUniformLocation(program_reference, projection_view_matrix_uniform)
        self.camera_position_reference = glGetUniformLocation(program_reference, camera_position_uniform)
    

    def get_view_matrix(self) -> np.ndarray:
        """Compute the view matrix from the camera."""

        # View matrix is the inverse of the camera's model matrix
        return np.linalg.inv(self.model_matrix)
    

    def get_projection_matrix(self, angle_of_view: float = 60, aspect_ratio: float = 1, near: float = 0.1, far: float = 1000) -> np.ndarray:
        """Generate a perspective projection matrix."""

        # Compute values for the perspective projection matrix and return
        a = angle_of_view * pi / 180.0
        d = 1.0 / tan(a / 2)
        r = aspect_ratio
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)
        return np.array([[d/r, 0, 0, 0],
                         [0, d, 0, 0],
                         [0, 0, b, c],
                         [0, 0, -1, 0]]).astype(np.float32)


    def activate(self) -> None:
        """Activate the camera by uploading its projection-view matrix and world position to the shader."""

        projection_view_matrix = self.get_projection_matrix() @ self.get_view_matrix()  # Combine projection and view matrices
        glUniformMatrix4fv(self.projection_view_matrix_reference, 1, GL_TRUE, projection_view_matrix)
        world_position = self.get_world_position()
        glUniform3f(self.camera_position_reference, world_position[0], world_position[1], world_position[2])
