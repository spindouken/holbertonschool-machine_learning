#!/usr/bin/env python3
"""
calculates the cost of a neural network with L2 regularization
"""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """
    cost: cost of the network without L2 regularization
    lambtha: regularization parameter
    weights: dictionary of the weights and biases
        (numpy.ndarrays) of the neural network
    L: number of layers in the neural network
    m: number of data points used
    Returns the cost of the network accounting for L2 regularization
    """
    sum_of_squared_weights = 0

    # calculate the sum of squared weights for each layer
    for layer_index in range(1, L + 1):
        sum_of_squared_weights += np.linalg.norm(
            weights['W' + str(layer_index)]
            ) ** 2

    regularization_term = lambtha / (2 * m) * sum_of_squared_weights

    Jreg = cost + regularization_term

    return Jreg
