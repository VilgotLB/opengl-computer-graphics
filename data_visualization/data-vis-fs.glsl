in vec3 color;
in vec2 fragPos;
in vec2 centerFragPos;
in float radius;

out vec4 fragColor;

void main() {
    float outerRadius = radius;
    float innerRadius = radius / 4;
    vec3 innerColor = vec3(1.0, 1.0, 0.0);
    
    // Determine whether the fragment is within the outer or inner radius
    float d = distance(fragPos, centerFragPos);
    float outerMask = step(d, outerRadius);
    float innerMask = step(d, innerRadius);

    // Color depending on if it's part of the inner or outer circle
    vec4 finalColor = vec4(color, outerMask);
    if (innerMask > 0.0) {
        finalColor = vec4(innerColor, innerMask);
    }

    fragColor = finalColor;
}
