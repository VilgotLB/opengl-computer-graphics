from solar_system.camera import Camera
from common.program import Program
from OpenGL.GL import *
from solar_system.celestial_body import CelestialBody
from math import pi

class SolarSystem(Program):
    """The solar system program."""

    # Shader program and variable configuration
    PROGRAM_NAME = 'Solar System'
    VERTEX_SHADER_FILE = 'solar_system/solar-system-vs.glsl'
    FRAGMENT_SHADER_FILE = 'solar_system/solar-system-fs.glsl'
    MODEL_MATRIX_UNIFORM = 'modelMatrix'
    PROJECTION_VIEW_MATRIX_UNIFORM = 'projectionViewMatrix'
    IS_SUN_UNIFORM = 'isSun'
    GLOSSINESS_UNIFORM = 'glossiness'
    CAMERA_POSITION_UNIFORM = 'cameraPosition'
    POSITION_VARIABLE = 'position'
    COLOR_VARIABLE = 'vertexColor'


    def __init__(self):
        """Initialize the SolarSystem program."""

        super().__init__(self.PROGRAM_NAME, self.VERTEX_SHADER_FILE, self.FRAGMENT_SHADER_FILE)


    def initialize_scene(self) -> None:
        """Set up the solar system scene with celestial bodies and a camera."""

        # Create, scale and position the celestial bodies (relative to their parent)
        self.sun = self.create_celestial_body([1.0, 1.0, 0.0], 0, True)
        self.sun.scale(3)

        self.planet1 = self.create_celestial_body([0.6, 0.0, 0.0], 80)
        self.planet1.scale(1/5)
        self.planet1.translate(-1.5, 0, 0, False)

        self.planet2 = self.create_celestial_body([0.2, 0.4, 0.2], 10)
        self.planet2.scale(1/3)
        self.planet2.translate(-2.5, 0, 0, False)

        self.planet3 = self.create_celestial_body([0.2, 0.2, 1.0], 30)
        self.planet3.scale(1/4)
        self.planet3.translate(-4, 0, 0, False)

        self.moon = self.create_celestial_body([0.5, 0.5, 0.5], 5)
        self.moon.scale(1/2)
        self.moon.translate(-3, 0, 0, False)

        self.planet4 = self.create_celestial_body([0.8, 0.2, 0.8], 100)
        self.planet4.scale(2/5)
        self.planet4.translate(-6, 0, 0, False)

        # Define the scene graph hierarchy for the celestial bodies
        self.sun.add_child(self.planet1)
        self.sun.add_child(self.planet2)
        self.sun.add_child(self.planet3)
        self.planet3.add_child(self.moon)
        self.sun.add_child(self.planet4)
        
        # Set up the camera
        camera = Camera(self.program, self.PROJECTION_VIEW_MATRIX_UNIFORM, self.CAMERA_POSITION_UNIFORM)
        camera.translate(0, 0, 35)
        camera.rotate_around_x(-pi / 4, False)
        camera.activate()

        glEnable(GL_CULL_FACE)  # Enable backface culling to optimize rendering
        glEnable(GL_DEPTH_TEST) # Enable depth testing for proper 3D rendering


    def update_scene(self, dt: float, time: float) -> None:
        """Update the solar system scene."""

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear buffers each frame

        # Rotate celestial bodies, both around their parent and their own axis
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

        # Render all celestial bodies
        self.sun.render()
        self.planet1.render()
        self.planet2.render()
        self.planet3.render()
        self.moon.render()
        self.planet4.render()
    

    def create_celestial_body(self, color: list[float], glossiness: float, is_sun: bool = False) -> CelestialBody:
        """Create a celestial body with specified properties."""

        return CelestialBody(self.program, self.MODEL_MATRIX_UNIFORM, self.GLOSSINESS_UNIFORM, self.IS_SUN_UNIFORM, self.POSITION_VARIABLE, self.COLOR_VARIABLE, color, glossiness, is_sun)
