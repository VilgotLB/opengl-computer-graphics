from camera import Camera
from program import Program
from OpenGL.GL import *
from celestial_body import CelestialBody
from math import pi

class SolarSystem(Program):

    PROGRAM_NAME = 'Solar System'
    VERTEX_SHADER_FILE = 'solar-system-vs.glsl'
    FRAGMENT_SHADER_FILE = 'solar-system-fs.glsl'
    MODEL_MATRIX_UNIFORM = 'modelMatrix'
    PROJECTION_VIEW_MATRIX_UNIFORM = 'projectionViewMatrix'
    POSITION_VARIABLE = 'position'
    COLOR_VARIABLE = 'vertexColor'


    def __init__(self):
        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self):
        self.sun = CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, [1.0, 1.0, 0.0])
        self.sun.scale(3)

        self.earth = CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, [0.2, 0.8, 0.5])
        self.earth.translate(-6, 0, 0)

        camera = Camera(self.program, self.PROJECTION_VIEW_MATRIX_UNIFORM)
        camera.rotate_around_x(-pi / 4)
        camera.translate(0, 10, 10)
        camera.activate()

        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)


    def update_scene(self, dt, time):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.sun.rotate_around_y(-dt)
        self.sun.render()

        self.earth.rotate_around_y(dt)
        self.earth.render()
