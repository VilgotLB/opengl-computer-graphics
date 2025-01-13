in vec3 color;
in vec2 fragPos;
in vec2 centerFragPos;
in float radius;

out vec4 fragColor;

void main() {
    float d = distance(fragPos, centerFragPos);
    
    float circleMask = step(d, radius);
    vec3 newColor = circleMask * color;

    fragColor = vec4(circleMask * color, 1.0);
}
