#!/usr/bin/env python3
"""
calculates the definiteness of a matrix
"""
import numpy as np


def definiteness(matrix):
    """
    matrix is a numpy.ndarray of shape (n, n)
        whose definiteness should be calculated
    If matrix is not a numpy.ndarray,
        raise a TypeError with the message:
            'matrix must be a numpy.ndarray'
    If matrix is not a valid matrix, return None

    Returns: the string Positive definite, Positive semi-definite,
        Negative semi-definite, Negative definite, or Indefinite
            if the matrix is positive definite, positive semi-definite,
            negative semi-definite, negative definite of indefinite
    If matrix does not fit any of the above categories, return None
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    rows, columns = matrix.shape
    if rows != columns:
        return None

    eigenvalues = np.linalg.eigvals(matrix)
    if all(eigenvalues > 0):
        return "Positive definite"
    elif all(eigenvalues >= 0):
        return "Positive semi-Definite"
    elif all(eigenvalues <= 0):
        return "Negative semi-Definite"
    elif all(eigenvalues < 0):
        return "Negative definite"
    elif any(eigenvalues > 0) and any(eigenvalues < 0):
        return "Indefinite"
    else:
        return None