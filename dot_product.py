def dot_product(v1, v2):
    """Calculates the dot product of two vectors.

    Args:
        v1 (list): The first vector.
        v2 (list): The second vector.

    Returns:
        float: The dot product of the two vectors.
    """

    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length.")

    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

v1 = [1, 2, 3]
v2 = [4, 5, 6]

print(dot_product(v1, v2))