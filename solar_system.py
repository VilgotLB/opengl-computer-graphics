from program import Program
import numpy as np
from OpenGL.GL import *
from matrix import Matrix
from sphere import generateSphere
from scene_object import SceneObject

class SolarSystem(Program):

    PROGRAM_NAME = 'Solar System'
    VERTEX_SHADER_FILE = 'solar-system-vs.glsl'
    FRAGMENT_SHADER_FILE = 'solar-system-fs.glsl'


    def __init__(self):
        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self):
        sphere_positions = generateSphere()

        self.sun = SceneObject(self.program, 'position', sphere_positions, 'vertexColor', [1.0, 1.0, 0.0] * len(sphere_positions))
        self.sun.translate(3, 1, 5)

        self.earth = SceneObject(self.program, 'position', sphere_positions, 'vertexColor', [0.0, 0.0, 1.0] * len(sphere_positions))
        self.earth.translate(-3, -3, -1)

        projection_matrix = Matrix.makePerspective()
        view_matrix = Matrix.makeTranslation(0,0,-10)
        projection_view_matrix = projection_matrix @ view_matrix

        projectionViewMatrix_reference = glGetUniformLocation(self.program, 'projectionViewMatrix')
        glUniformMatrix4fv(projectionViewMatrix_reference, 1, GL_TRUE, projection_view_matrix)


    def update_scene(self):
        self.sun.render()
        self.earth.render()
