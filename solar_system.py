from camera import Camera
from program import Program
import numpy as np
from OpenGL.GL import *
from matrix import Matrix
from sphere import generateSphere
from scene_object import SceneObject
from math import pi

class SolarSystem(Program):

    PROGRAM_NAME = 'Solar System'
    VERTEX_SHADER_FILE = 'solar-system-vs.glsl'
    FRAGMENT_SHADER_FILE = 'solar-system-fs.glsl'


    def __init__(self):
        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self):
        sphere_positions = generateSphere()

        self.sun = SceneObject(self.program, 'modelMatrix', 'position', sphere_positions, 'vertexColor', [1.0, 1.0, 0.0] * len(sphere_positions))
        self.sun.scale(3)

        self.earth = SceneObject(self.program, 'modelMatrix', 'position', sphere_positions, 'vertexColor', [0.0, 0.0, 1.0] * len(sphere_positions))
        self.earth.translate(-6, 0, 0)

        camera = Camera(self.program, 'projectionViewMatrix')
        camera.rotate_around_x(-pi / 4)
        camera.translate(0, 10, 10)
        camera.activate()

        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)


    def update_scene(self, dt, time):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.sun.render()

        self.earth.rotate_around_y(dt)
        self.earth.render()
