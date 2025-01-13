in vec3 color;
in vec2 fragPos;
in vec2 centerFragPos;
in float radius;

out vec4 fragColor;

void main() {
    float d = distance(fragPos, centerFragPos);
    float colorMask = step(d, radius);
    fragColor = vec4(colorMask * color, 1.0);
}
