in vec3 position;
in vec3 centerPos;
in vec3 vertexColor;

uniform mat4 transformation;

out vec3 color;
out vec2 fragPos;
out vec2 centerFragPos;
out float radius;

void main() {
    vec4 newPos = transformation * vec4(position, 1.0);
    gl_Position = newPos;
    fragPos = vec2(newPos);
    
    vec4 newCenter = transformation * vec4(centerPos, 1.0);
    centerFragPos = vec2(newCenter);

    // Radius should be the half-length of the quad
    radius = abs(newPos.x - newCenter.x);

    color = vertexColor;
}
