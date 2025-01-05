uniform bool isSun;
uniform float glossiness;

in vec3 normal;
in vec3 sunDirection;
in vec3 cameraDirection;
in vec3 color;

out vec4 fragColor;

void main() {
  vec3 lightColor = vec3(1.0, 1.0, 0.8);
  vec3 ambientColor = vec3(0.1, 0.1, 0.1);

  vec3 finalColor;

  if (isSun) {
    finalColor = color;
  } else {
    vec3 ambientComponent = ambientColor * color;

    float diffuseIntensity = max(dot(normal, sunDirection), 0.0);
    vec3 diffuseComponent = lightColor * diffuseIntensity * color;

    vec3 reflectionDirection = reflect(-sunDirection, normal);
    float specularIntensity = pow(max(dot(cameraDirection, reflectionDirection), 0.0), glossiness);
    vec3 specularComponent = lightColor * specularIntensity;
    
    finalColor = ambientComponent + diffuseComponent + specularComponent;
  }
  
  fragColor = vec4(finalColor, 1.0);
}