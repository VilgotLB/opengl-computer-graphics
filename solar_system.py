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

        self.planet1 = CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, [0.6, 0.0, 0.0])
        self.planet1.scale(1/5)
        self.planet1.translate(-1.5, 0, 0, False)

        self.planet2 = CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, [0.2, 0.4, 0.2])
        self.planet2.scale(1/3)
        self.planet2.translate(-2.5, 0, 0, False)

        self.planet3 = CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, [0.2, 0.2, 1.0])
        self.planet3.scale(1/4)
        self.planet3.translate(-4, 0, 0, False)

        self.moon = CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, [0.5, 0.5, 0.5])
        self.moon.scale(1/2)
        self.moon.translate(-3, 0, 0, False)

        self.planet4 = CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, [0.8, 0.2, 0.8])
        self.planet4.scale(3/5)
        self.planet4.translate(-7, 0, 0, False)

        self.sun.add_child(self.planet1)
        self.sun.add_child(self.planet2)
        self.sun.add_child(self.planet3)
        self.planet3.add_child(self.moon)
        self.sun.add_child(self.planet4)
        
        camera = Camera(self.program, self.PROJECTION_VIEW_MATRIX_UNIFORM)
        camera.rotate_around_x(-pi / 6)
        camera.translate(0, 20, 35, False)
        camera.activate()

        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)


    def update_scene(self, dt, time):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.planet1.rotate_around_y(dt * pi/4, False)
        self.planet1.rotate_around_y(dt * pi/4, True)

        self.planet2.rotate_around_y(dt * pi/2, False)
        self.planet2.rotate_around_y(dt * -pi, True)

        self.planet3.rotate_around_y(dt * pi/6, False)
        self.planet3.rotate_around_y(dt * pi/3, True)

        self.moon.rotate_around_y(dt * pi/8, False)
        self.moon.rotate_around_y(dt * -pi, True)

        self.planet4.rotate_around_y(dt * pi/20, False)
        self.planet4.rotate_around_y(dt * -pi/4, True)

        self.sun.render()
        self.planet1.render()
        self.planet2.render()
        self.planet3.render()
        self.moon.render()
        self.planet4.render()
