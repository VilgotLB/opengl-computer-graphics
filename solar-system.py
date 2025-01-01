import pygame
import numpy as np
from OpenGL.GL import *

def run(program_name, vertex_shader_file, fragment_shader_file):
    setup_pygame(program_name)
    vertex_shader = initialize_shader(vertex_shader_file, GL_VERTEX_SHADER)
    fragment_shader = initialize_shader(fragment_shader_file, GL_FRAGMENT_SHADER)
    program = initialize_program(vertex_shader, fragment_shader)
    glUseProgram(program)

    initialize_scene(program)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        update_scene()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()


def setup_pygame(program_name):
    screen_size = [512, 512]
    display_flags = pygame.DOUBLEBUF | pygame.OPENGL

    pygame.init()
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
    pygame.display.set_mode(screen_size, display_flags)
    pygame.display.set_caption(program_name)


def initialize_shader(shader_file, shader_type):
    shader_code = '#version 330\n'
    with open(shader_file, encoding='utf-8') as file:
        shader_code += file.read()

    shader_reference = glCreateShader(shader_type)
    glShaderSource(shader_reference, shader_code)
    glCompileShader(shader_reference)

    compile_successful = glGetShaderiv(shader_reference, GL_COMPILE_STATUS)
    if not compile_successful:
        error_message = glGetShaderInfoLog(shader_reference)
        glDeleteShader(shader_reference)
        error_message = '\n' + error_message.decode('utf-8')
        raise Exception(error_message)
    
    return shader_reference


def initialize_program(vertex_shader, fragment_shader):
    program_reference = glCreateProgram()
    glAttachShader(program_reference, vertex_shader)
    glAttachShader(program_reference, fragment_shader)
    glLinkProgram(program_reference)

    link_successful = glGetProgramiv(program_reference, GL_LINK_STATUS)
    if not link_successful:
        error_message = glGetProgramInfoLog(program_reference)
        glDeleteProgram(program_reference)
        error_message = '\n' + error_message.decode('utf-8')
        raise Exception(error_message)
    
    return program_reference


def initialize_scene(program):
    vao_reference = glGenVertexArrays(1)
    glBindVertexArray(vao_reference)
    
    positions = [0.0, 0.8, 0.0,
                 0.8, -0.8, 0.0,
                 -0.8, -0.8, 0.0]
    
    vertex_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
    glBufferData(GL_ARRAY_BUFFER, np.array(positions, dtype=np.float32), GL_STATIC_DRAW)
    position_variable_reference = glGetAttribLocation(program, 'position')
    glVertexAttribPointer(position_variable_reference, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(position_variable_reference)


def update_scene():
    glDrawArrays(GL_TRIANGLES, 0, 3)


run('TEST', 'solar-system-vs.glsl', 'solar-system-fs.glsl')
