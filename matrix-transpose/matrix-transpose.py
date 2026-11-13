import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    # python transpose fucntion
    matrix = np.array(A) # convert to a numpy array
    transposed = matrix.T
    return transposed

