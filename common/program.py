import pygame
from OpenGL.GL import *
from abc import ABC, abstractmethod

class Program(ABC):
    """Abstract base class for an OpenGL rendering program using Pygame."""

    def __init__(self, program_name: str, vertex_shader_file: str, fragment_shader_file: str):
        """Initialize the program with a name and shader file paths."""

        self.program_name = program_name
        self.vertex_shader_file = vertex_shader_file
        self.fragment_shader_file = fragment_shader_file


    def run(self) -> None:
        """Run the program."""

        # Set up the program
        self.setup_pygame()
        vertex_shader = self.initialize_shader(self.vertex_shader_file, GL_VERTEX_SHADER)
        fragment_shader = self.initialize_shader(self.fragment_shader_file, GL_FRAGMENT_SHADER)
        self.program = self.initialize_program(vertex_shader, fragment_shader)
        glUseProgram(self.program)

        self.initialize_scene()

        # Start the program loop
        clock = pygame.time.Clock()
        time = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            dt = clock.tick(60) / 1000.0
            time += dt
            self.update_scene(dt, time)

            pygame.display.flip()

        pygame.quit()


    def setup_pygame(self) -> None:
        """Configure the Pygame window and OpenGL context."""

        screen_size = [512, 512]
        display_flags = pygame.DOUBLEBUF | pygame.OPENGL    # Enable double buffering for smooth rendering.

        # Create the window and set its properties.
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.set_mode(screen_size, display_flags)
        pygame.display.set_caption(self.program_name)


    def initialize_shader(self, shader_file: str, shader_type: int) -> int:
        """Compile a shader from the provided source file."""

        # Start the shader source with a version declaration.
        shader_code = '#version 330\n'
        with open(shader_file, encoding='utf-8') as file:
            shader_code += file.read()

        # Compile the shader
        shader_reference = glCreateShader(shader_type)
        glShaderSource(shader_reference, shader_code)
        glCompileShader(shader_reference)

        # Check if the shader compiled successfully.
        compile_successful = glGetShaderiv(shader_reference, GL_COMPILE_STATUS)
        if not compile_successful:
            error_message = glGetShaderInfoLog(shader_reference)
            glDeleteShader(shader_reference)
            error_message = '\n' + error_message.decode('utf-8')
            raise Exception(error_message)
        
        return shader_reference


    def initialize_program(self, vertex_shader: int, fragment_shader: int) -> int:
        """Link vertex and fragment shaders into a complete shader program."""

        # Create a program to link the shaders.
        program_reference = glCreateProgram()
        glAttachShader(program_reference, vertex_shader)
        glAttachShader(program_reference, fragment_shader)
        glLinkProgram(program_reference)

        # Check if the program linked successfully.
        link_successful = glGetProgramiv(program_reference, GL_LINK_STATUS)
        if not link_successful:
            error_message = glGetProgramInfoLog(program_reference)
            glDeleteProgram(program_reference)
            error_message = '\n' + error_message.decode('utf-8')
            raise Exception(error_message)
        
        return program_reference


    @abstractmethod
    def initialize_scene(self) -> None:
        """Set up the OpenGL scene. This method is called once, immediately after running the program."""
        pass

    @abstractmethod
    def update_scene(self, dt: float, time: float) -> None:
        """Update the OpenGL scene each frame."""
        pass
