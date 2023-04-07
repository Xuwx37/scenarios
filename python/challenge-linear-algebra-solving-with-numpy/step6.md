# Matrix Rank Calculation

## TODO

Write a Python function `matrix_rank(matrix)` in `matrix_rank.py` that takes a NumPy matrix as input and calculates its rank. The function should return the rank of the matrix as an integer.

- The `numpy.linalg.matrix_rank(matrix)` function is used to return the rank of the `matrix` as an integer.

## Example Input

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

C = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

print(matrix_rank(A))

print(matrix_rank(B))

print(matrix_rank(C))
```

## Example Output

```lua
2
2
2
```
