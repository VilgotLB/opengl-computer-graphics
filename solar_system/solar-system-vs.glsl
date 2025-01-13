uniform mat4 projectionViewMatrix;
uniform mat4 modelMatrix;
uniform vec3 cameraPosition;

in vec3 position;
in vec3 vertexColor;

out vec3 normal;
out vec3 sunDirection;
out vec3 cameraDirection;
out vec3 color;

void main() {
    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
    gl_Position = projectionViewMatrix * worldPosition;

    // Extract the rotation part of the model matrix for normal transformation
    mat3 rotationMatrix = mat3(modelMatrix);
    rotationMatrix[0] = normalize(rotationMatrix[0]);
    rotationMatrix[1] = normalize(rotationMatrix[1]);
    rotationMatrix[2] = normalize(rotationMatrix[2]);

    // Transform the normal vector to world space (only rotations should affect the normal)
    // Also, it's a unit sphere, so position is the same as normal
    normal = rotationMatrix * position.xyz;

    // Calculate the direction to the sun (at origin)
    sunDirection = normalize(-worldPosition.xyz);

    // Calculate the direction to the camera
    cameraDirection = normalize(cameraPosition - worldPosition.xyz);

    color = vertexColor;
}