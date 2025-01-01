uniform mat4 projectionViewMatrix;
in vec3 position;
void main() {
    gl_Position = projectionViewMatrix * vec4(position, 1.0);
}