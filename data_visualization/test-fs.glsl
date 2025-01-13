in vec3 color;
in vec2 fragPos;
in vec2 centerFragPos;
in float radius;

out vec4 fragColor;

void main() {
    float outerRadius = radius;
    float innerRadius = 0.01;
    vec3 innerColor = vec3(0.0, 0.3, 0.0);

    float d = distance(fragPos, centerFragPos);
    
    float outerMask = step(d, outerRadius);
    float innerMask = step(d, innerRadius);

    vec3 finalColor = outerMask * color;
    if (innerMask > 0.0) {
        finalColor = innerMask * innerColor;
    }

    fragColor = vec4(finalColor, 1.0);
}
