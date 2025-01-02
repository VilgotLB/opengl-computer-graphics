uniform mat4 projectionViewMatrix;
uniform mat4 modelMatrix;
in vec3 position;

void main() {
    gl_Position = projectionViewMatrix * modelMatrix * vec4(position, 1.0);
}