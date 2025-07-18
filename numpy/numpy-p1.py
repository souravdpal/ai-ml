import numpy as np  

# First, we create a 1D NumPy array (vector)
array = np.array([1, 2, 3, 4, 5])
print("Simple array:", array)

# In Python, [] normally creates a list.
# But with NumPy, np.array() turns lists into powerful arrays (vectors, matrices, tensors)

"""
Shapes in NumPy:
  - Scalar: A single number, e.g., 2
  - 1D Vector: [1, 2, 3]
  - 2D Matrix: [[1, 2], [3, 4]]
  - 3D Tensor: [[[...]], [[...]]]

Important:
  When creating 2D or 3D arrays, all inner arrays must have the same length.
  You can't mix [1,2,3] with [1,2] — NumPy will throw a ValueError.
"""

# Create a 1D Vector
vector_1d = np.array([1, 2, 3, 4, 5, 5])
print(f"\nVector:\n{vector_1d}")

# Create a 2D Matrix (2 rows x 8 columns)
matrix_2d = np.array([
    [1, 1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 8, 9, 7, 4, 5]
])
print(f"\nMatrix:\n{matrix_2d}")

# Create a 3D Tensor (2 x 1 x 7)
tensor_3d = np.array([
    [[1, 2, 3, 4, 5, 8, 6]],
    [[2, 3, 4, 5, 6, 7, 2]]
])
print(f"\nTensor:\n{tensor_3d}")
