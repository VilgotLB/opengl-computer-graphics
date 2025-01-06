in vec3 position;
in vec3 vertexColor;

uniform mat4 graphTransformation;

out vec3 color;

void main() {
    gl_Position = graphTransformation * vec4(position, 1.0);
    color = vertexColor;
}
