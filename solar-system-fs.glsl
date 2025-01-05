uniform bool isSun;

in vec3 normal;
in vec3 sunDirection;
in vec3 color;

out vec4 fragColor;

void main() {
  vec3 lightColor = vec3(1.0, 1.0, 0.8);
  vec3 ambientColor = vec3(0.1, 0.1, 0.1);

  vec3 finalColor;

  if (isSun) {
    finalColor = color;
  } else {
    float diffuseIntensity = max(dot(normal, sunDirection), 0.0);
    finalColor = ambientColor * color + lightColor * diffuseIntensity * color;
  }
  
  fragColor = vec4(finalColor, 1.0);
}