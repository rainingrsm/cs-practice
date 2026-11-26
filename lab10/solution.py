import numpy as np


def make_table(rows: int, columns: int) -> list[list[int]]:
    numbers = np.arange(rows * columns)
    return numbers.reshape(rows, columns).tolist()


def rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int,
) -> list[list[float]]:
    array = np.array(matrix)
    return array[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int,
    value: float,
) -> list[list[float]]:
    result = np.asarray(matrix, dtype=float).copy()
    result[row_start:row_stop, column_start:column_stop] = value
    return result.tolist()


def matrix_vector_product(
    matrix: list[list[float]], vector: list[float]
) -> list[float]:
    result = np.array(matrix) @ np.array(vector)
    return result.tolist()


def matrix_multiply(
    left: list[list[float]], right: list[list[float]]
) -> list[list[float]]:
    result = np.array(left) @ np.array(right)
    return result.tolist()


def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return np.array(matrix).T.tolist()


def solve_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    result = np.linalg.solve(matrix, vector)
    return result.round(6).tolist()


def tensor_channel_mean(tensor: list) -> list:
    return np.array(tensor).mean(axis=-1).tolist()


def point_distance(first: list[float], second: list[float]) -> float:
    difference = np.array(first, dtype=float) - np.array(second, dtype=float)
    return round(float(np.linalg.norm(difference)), 6)
