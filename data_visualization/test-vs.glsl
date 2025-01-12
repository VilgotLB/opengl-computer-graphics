in vec3 position;
in vec3 vertexColor;

uniform mat4 transformation;

out vec3 color;
out vec2 fragPos;

void main() {
    vec4 newPos = transformation * vec4(position, 1.0);
    gl_Position = newPos;
    fragPos = vec2(newPos);
    
    color = vertexColor;
}
