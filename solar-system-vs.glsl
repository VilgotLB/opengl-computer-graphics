uniform mat4 projectionViewMatrix;
uniform mat4 modelMatrix;

in vec3 position;
in vec3 vertexColor;

out vec3 normal;
out vec3 sunDirection;
out vec3 color;

void main() {
    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
    gl_Position = projectionViewMatrix * worldPosition;

    mat3 rotationMatrix = mat3(modelMatrix);
    rotationMatrix[0] = normalize(rotationMatrix[0]);
    rotationMatrix[1] = normalize(rotationMatrix[1]);
    rotationMatrix[2] = normalize(rotationMatrix[2]);

    normal = rotationMatrix * position.xyz;
    sunDirection = normalize(-worldPosition.xyz);
    color = vertexColor;
}