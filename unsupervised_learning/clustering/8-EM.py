#!/usr/bin/env python3
"""
performs the expectation maximization for a GMM
"""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000,
                             tol=1e-5, verbose=False):
    """
    X is a numpy.ndarray of shape (n, d) containing the data set
    k is a positive integer containing the number of clusters
    iterations is a positive integer containing the maximum number of
        iterations for the algorithm
    tol is a non-negative float containing tolerance of the log likelihood,
        used to determine early stopping i.e. if the difference is less than or
        equal to tol you should stop the algorithm
    verbose is a boolean that determines if you should print information about
        the algorithm
    If True, print:
        'Log Likelihood after {i} iterations: {l}'
        every 10 iterations and after the last iteration
            {i} is the number of iterations of the EM algorithm
            {l} is the log likelihood, rounded to 5 decimal places

    Returns: pi, m, S, g, l, or None, None, None, None, None on failure
        pi is a numpy.ndarray of shape (k,) containing the priors for each
            cluster
        m is a numpy.ndarray of shape (k, d) containing the centroid means for
            each cluster
        S is a numpy.ndarray of shape (k, d, d) containing the covariance
            matrices for each cluster
        g is a numpy.ndarray of shape (k, n) containing the probabilities for
            each data point in each cluster
        l is the log likelihood of the model
    """
    if (
        not isinstance(X, np.ndarray)
        or not isinstance(k, int)
        or not isinstance(iterations, int)
        or not isinstance(tol, float)
        or not isinstance(verbose, bool)
    ):
        return None, None, None, None, None

    if (
        len(X.shape) != 2
        or k < 1
        or iterations < 1
    ):
        return None, None, None, None, None
