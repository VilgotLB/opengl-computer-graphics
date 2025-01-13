import numpy as np
from OpenGL.GL import *
from common.scene_entity import SceneEntity

class SceneObject(SceneEntity):
    """Represents a drawable object in an OpenGL scene."""

    def __init__(self, program_reference: int, model_matrix_uniform: str, position_variable_name: str, positions: list[list[float]], color_variable_name: str, colors: list[list[float]]):
        """Initialize a SceneObject with vertex data and shader program references, to prepare it for rendering."""

        super().__init__()

        self.program = program_reference
        self.number_of_vertices = len(positions)

        # Generate and bind a Vertex Array Object (VAO) for the object
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        # Store vertex positions and colors as attributes in vertex buffers.
        self.store_vertex_attribute(self.program, position_variable_name, positions)
        self.store_vertex_attribute(self.program, color_variable_name, colors)

        # Get the location of the model matrix uniform in the shader program
        self.modelMatrix_reference = glGetUniformLocation(self.program, model_matrix_uniform)
    

    def store_vertex_attribute(self, program: int, variable_name: str, data: list[list[float]]) -> None:
        """Store vertex attribute data in a vertex buffer."""

        data = np.array(data).ravel().astype(np.float32)

        # Create a new buffer, bind it, and upload the data
        vertex_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, data, GL_STATIC_DRAW)

        # Specify how the data is structured and enable the attribute
        variable_reference = glGetAttribLocation(program, variable_name)
        glVertexAttribPointer(variable_reference, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(variable_reference)


    def render(self) -> None:
        """Render the SceneObject"""

        # Bind the VAO for this object
        glBindVertexArray(self.vao)

        # Update the model matrix uniform in the shader to this object's model matrix
        glUniformMatrix4fv(self.modelMatrix_reference, 1, GL_TRUE, self.get_world_matrix())

        # Draw the object
        glDrawArrays(GL_TRIANGLES, 0, self.number_of_vertices)
