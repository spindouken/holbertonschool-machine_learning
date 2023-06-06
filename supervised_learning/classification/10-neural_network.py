#!/usr/bin/env python3
"""creating nodes in a network.... networking....a neural network"""
import numpy as np


class NeuralNetwork:
    """
    defines a neural network with one hidden layer
    performing binary classification
    """
    def __init__(self, nx, nodes):
        """
        initialize a neural network
        nx: the number of input features
        nodes: the number of nodes found in the hidden layer
        W1: The weights vector of the hidden layer.
            initialized using a random normal distribution.
        b1: The bias of the hidden layer. Initialized with 0’s.
        A1: The activated output of the hidden layer. Initialized to 0.
        W2: The weights vector of the output neuron.
            Initialized using a random normal distribution.
        b2: The bias of the output neuron. Initialized to 0.
        A2: The activated output of the output neuron (prediction).
            Initialized to 0.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros(shape=(nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        return self.__W1

    @property
    def b1(self):
        return self.__b1

    @property
    def A1(self):
        return self.__A1

    @property
    def W2(self):
        return self.__W2

    @property
    def b2(self):
        return self.__b2

    @property
    def A2(self):
        return self.__A2

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neural network
        X: numpy.ndarray of shape (nx, m) that contains the input data
        nx: number of input features to the neuron
        m: number of examples
        Returns the private attributes __A1 and __A2
        """
        # Z1 is the result of the dot product
        #   of weights and input data plus the bias
        # Represents the input of the activation function of the hidden layer
        Z1 = np.matmul(self.__W1, X) + self.__b1

        # Apply the sigmoid activation function to Z1 to get A1
        # The sigmoid function transforms the input to a value
        #   between 0 and 1 which can be interpreted as a probability
        self.__A1 = 1 / (1 + np.exp(-Z1))

        # Z2 is the result of the dot product
        #   of weights and the output of the hidden layer plus the bias
        # Represents the input of the activation function of the output neuron
        Z2 = np.matmul(self.__W2, self.__A1) + self.__b2

        # Apply the sigmoid activation function to Z2 to get A2
        # The sigmoid function transforms the input to a value
        #   between 0 and 1 which can be interpreted as a probability
        self.__A2 = 1 / (1 + np.exp(-Z2))

        return self.__A1, self.__A2
