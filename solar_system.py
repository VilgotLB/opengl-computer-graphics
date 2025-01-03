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
        self.planet1 = CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, [0.2, 0.8, 0.5])
        self.moon = CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, [0.8, 0.3, 0.8])
        self.sun.add_child(self.planet1)
        self.planet1.add_child(self.moon)

        self.sun.scale(2)
        self.planet1.scale(1/2)

        self.moon.translate(0, 0, 3)
        self.planet1.translate(-10, 0, 0)

        self.moon.scale(3/4)
        
        camera = Camera(self.program, self.PROJECTION_VIEW_MATRIX_UNIFORM)
        camera.rotate_around_x(-pi / 2)
        camera.translate(0, 30, 0, False)
        camera.activate()

        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)


    def update_scene(self, dt, time):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.planet1.rotate_around_y(dt * pi, False)
        self.moon.rotate_around_y(dt * pi, False)

        self.sun.render()
        self.planet1.render()
        self.moon.render()
