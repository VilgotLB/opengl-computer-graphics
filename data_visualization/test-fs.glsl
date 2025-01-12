in vec3 color;
in vec2 fragPos;
out vec4 fragColor;

void main() {
    float d = distance(fragPos, vec2(0.0, 0.0));
    float colorMask = step(d, 0.8);
    fragColor = vec4(colorMask * color, 1.0);
}
