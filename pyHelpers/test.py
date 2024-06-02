import numpy as np

def compute_normal(v1, v2, v3):
    # Compute vectors
    vector1 = np.subtract(v2, v1)
    vector2 = np.subtract(v3, v1)
    # Cross product
    normal = np.cross(vector1, vector2)
    # Normalize
    normal_length = np.linalg.norm(normal)
    normal = normal / normal_length if normal_length != 0 else normal
    return normal

# Example vertices (for simplicity, a few)
vertices = np.array([      
    # Front face
      # [-1.0, -1.0, 1.0],
      # [1.0, -1.0, 1.0],
      # [1.0, 1.0, 1.0],
      # [-1.0, 1.0, 1.0],
      # # Back face
      # [-1.0, -1.0, -1.0],
      # [-1.0, 1.0, -1.0],
      # [1.0, 1.0, -1.0],
      # [1.0, -1.0, -1.0],
      # # Top face
      # [-1.0, 1.0, -1.0],
      # [-1.0, 1.0, 1.0],
      # [1.0, 1.0, 1.0],
      # [1.0, 1.0, -1.0],
      # # Bottom face
      # [-1.0, -1.0, -1.0],
      # [1.0, -1.0, -1.0],
      # [1.0, -1.0, 1.0],
      # [-1.0, -1.0, 1.0],
      # # Right face
      # [1.0, -1.0, -1.0],
      # [1.0, 1.0, -1.0],
      # [1.0, 1.0, 1.0],
      # [1.0, -1.0, 1.0],
      # # Left face
      # [-1.0, -1.0, -1.0],
      # [-1.0, -1.0, 1.0],
      # [-1.0, 1.0, 1.0],
      # [-1.0, 1.0, -1.0]

[-0.728036, 0.285, 0.0], 
[-0.728036, -0.132, 0.0], 
[-0.723295, -0.147, 0.0], 
[-0.71065, -0.155, 0.0], 
[-0.68694, -0.157, 0.0], 
[-0.658489, -0.144, 0.0], 
[-0.667183, -0.155, 0.0], 
[-0.655328, -0.128, 0.0], 
[-0.655328, 0.285, 0.0], 
[-0.722504, 0.279467, 0.06], 
[-0.728036, 0.285, 0.054591], 
[-0.728036, -0.112892, 0.054591], 
[-0.722504, -0.110145, 0.06], 
[-0.723295, -0.127887, 0.054604], 
[-0.718628, -0.122403, 0.06], 
[-0.71065, -0.135883, 0.054617], 
[-0.708835, -0.128599, 0.06], 
[-0.68694, -0.137882, 0.054619], 
[-0.686987, -0.130442, 0.06], 
[-0.658489, -0.124891, 0.054593], 
[-0.663658, -0.120616, 0.06], 
[-0.670071, -0.12873, 0.06], 
[-0.667183, -0.135885, 0.05461], 
[-0.655328, -0.108895, 0.05458], 
[-0.660861, -0.106457, 0.06], 
[-0.655328, 0.285, 0.054591], 
[-0.660861, 0.279467, 0.06],# Add remaining vertices...
])

# Example faces (defined by indices into the vertices array)
faces = [
          #Front face
      # [0, 1, 2], [0, 2, 3],
      # #Back face
      # [4, 5, 6], [4, 6, 7],
      # #Top face
      # [8, 9, 10], [8, 10, 11],
      # #Bottom face
      # [12, 13, 14], [12, 14, 15],
      # #Right face
      # [16, 17, 18], [16, 18, 19],
      # #Left face
      # [20, 21, 22], [20, 22, 23]
[5, 22, 6], 
[3, 17, 15], 
[8, 23, 7], 
[6, 17, 4], 
[1, 13, 11], 
[7, 19, 5], 
[2, 15, 13], 
[0, 11, 10], 
[8, 10, 0], 
[3, 2, 1], 
[11, 9, 10], 
[11, 14, 12], 
[13, 16, 14], 
[17, 16, 15], 
[19, 21, 22], 
[17, 21, 18], 
[23, 20, 19], 
[23, 26, 24], 
[26, 10, 9], 
[20, 24, 18], 
[5, 19, 22], 
[3, 4, 17], 
[8, 25, 23], 
[6, 22, 17], 
[1, 2, 13], 
[7, 23, 19], 
[2, 3, 15], 
[0, 1, 11], 
[8, 25, 10], 
[1, 0, 7], 
[0, 8, 7], 
[7, 5, 4], 
[1, 7, 4], 
[5, 6, 4], 
[4, 3, 1], 
[11, 12, 9], 
[11, 13, 14], 
[13, 15, 16], 
[17, 18, 16], 
[19, 20, 21], 
[17, 22, 21], 
[23, 24, 20], 
[23, 25, 26], 
[26, 25, 10], 
[26, 9, 24], 
[9, 12, 24], 
[12, 14, 16], 
[16, 18, 12], 
[18, 21, 20], 
[12, 18, 24]
    # Add remaining faces...
]

# Initialize normals
normals = np.zeros((len(vertices), 3))

# Compute normals for each face
face_normals = []
for face in faces:
    v1, v2, v3 = vertices[face]
    normal = compute_normal(v1, v2, v3)
    face_normals.append(normal)
    # Add normal to each vertex in the face
    for idx in face:
        normals[idx] += normal

# Normalize vertex normals
for i in range(len(normals)):
    normals[i] = normals[i] / np.linalg.norm(normals[i]) if np.linalg.norm(normals[i]) != 0 else normals[i]

# Print results
print("Vertex Normals:")
print(normals)
print(len(normals))


#chatGPT as a last resort. di man din gumana