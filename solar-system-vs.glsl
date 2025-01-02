uniform mat4 projectionViewMatrix;
uniform mat4 modelMatrix;
in vec3 position;
in vec3 vertexColor;
out vec3 color;

void main() {
    gl_Position = projectionViewMatrix * modelMatrix * vec4(position, 1.0);
    color = vertexColor;
}