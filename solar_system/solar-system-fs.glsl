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

    // Point light is inside the sun, which means its surface would never be lit, so the base color is used.
    if (isSun) {
        finalColor = color;
    } else {
        // Ambient lighting component
        vec3 ambientComponent = ambientColor * color;

        // Diffuse lighting component
        float diffuseIntensity = max(dot(normal, sunDirection), 0.0);
        vec3 diffuseComponent = lightColor * diffuseIntensity * color;

        // Specular lighting component
        vec3 reflectionDirection = reflect(-sunDirection, normal);
        float specularIntensity = pow(max(dot(cameraDirection, reflectionDirection), 0.0), glossiness);
        vec3 specularComponent = lightColor * specularIntensity;
        
        // Combine lighting components for the final color
        finalColor = ambientComponent + diffuseComponent + specularComponent;
    }

    fragColor = vec4(finalColor, 1.0);
}