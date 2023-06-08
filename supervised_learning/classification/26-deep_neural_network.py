#!/usr/bin/env python3
"""are you winning at neural networks son?"""
import pickle
import numpy as np
import matplotlib.pyplot as plt


class DeepNeuralNetwork:
    """
    defines a deep neural network performing binary classification
    """
    def __init__(self, nx, layers):
        """
        L: number of layers in the neural network
        cache: A dictionary to hold all intermediary values of the network.
            Upon instantiation, it is set to an empty dictionary
        weights: A dictionary to hold all weights and biases of the network
            Upon instantiation,
            weights initialized using He et al. method
                and saved in the weights dictionary using the key W{1}
                    where {1} is the hidden layer the weight belongs to
            biases initialized to 0's and saved
                in the weights dictionary using the key b{1}
                    where {1} is the hiddne layer the bias belongs to
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or not layers:
            raise TypeError("layers must be a list of positive integers")
        if not all(map(lambda x: isinstance(x, int) and x > 0, layers)):
            raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(self.__L):
            self.__weights['W' + str(i+1)] = np.random.randn(
                layers[i], nx) * np.sqrt(2/nx)
            self.__weights['b' + str(i+1)] = np.zeros((layers[i], 1))
            nx = layers[i]

    @property
    def L(self):
        return self.__L

    @property
    def cache(self):
        return self.__cache

    @property
    def weights(self):
        return self.__weights

    def forward_prop(self, X):
        """Forward Propagation"""
        self.__cache['A0'] = X
        for i in range(1, self.__L + 1):
            Zi = np.dot(self.__weights['W' + str(i)],
                        self.__cache['A' + str(i - 1)]) +\
                        self.__weights['b' + str(i)]
            self.__cache['A' + str(i)] = self.sigmoid(Zi)
        return self.__cache['A' + str(self.__L)], self.__cache

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        Y: a numpy.ndarray with shape (1, m)
            that contains the correct labels of the input data
        A: a numpy.ndarray with shape (1, m)
            containing the activated output of the neuron of each example
        Returns the cost of the model as a float
        """
        m = Y.shape[1]
        cost = -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neural network's predictions
        X: a numpy.ndarray with shape (nx, m) that contains the input data
        Y: a numpy.ndarray with shape (1, m)
            that contains the correct labels of the input data
        Returns the neuron's prediction and the cost of the network
        """
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neural network
        Y: a numpy.ndarray with shape (1, m)
            that contains the correct labels of the input data
        cache: a dictionary containing all intermediary values of the network
        alpha: the learning rate
        Updates the private attribute __weights
        """
        m = Y.shape[1]
        for i in reversed(range(1, self.__L + 1)):
            A = cache['A' + str(i)]
            A_prev = cache['A' + str(i - 1)]
            W = self.__weights['W' + str(i)]
            if i == self.__L:
                dz = A - Y
            else:
                dz = da * self.sigmoid_derivative(A)
            dw = np.dot(dz, A_prev.T) / m
            db = np.sum(dz, axis=1, keepdims=True) / m
            if i > 1:
                da = np.dot(W.T, dz)
            self.__weights['W' + str(i)] -= alpha * dw
            self.__weights['b' + str(i)] -= alpha * db

    def train(self, X, Y, iterations=5000,
              alpha=0.05, verbose=True, graph=True, step=100):
        """
        Trains the deep neural network
        X: a numpy.ndarray with shape
            (nx, m) that contains the input data
        Y: a numpy.ndarray with shape (1, m)
            that contains the correct labels of the input data
        iterations: the number of iterations to train over
        alpha: the learning rate
        verbose: boolean that defines whether or not
            to print information about the training
        graph: boolean that defines whether or not
            to graph information about the training
        step: the interval of printing information and updating the graph
        Updates the private attributes __weights and __cache
        Returns the evaluation of the training data
            after iterations of training have occurred
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 1:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        if verbose is True or graph is True:
            if not isinstance(step, int):
                raise TypeError("step must be an integer")
            if step <= 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")
        costs = []
        for i in range(iterations):
            A, cache = self.forward_prop(X)
            self.gradient_descent(Y, cache, alpha)
            if i % step == 0 or i == iterations:
                cost = self.cost(Y, A)
                costs.append(cost)
                if verbose is True:
                    print("Cost after {} iterations: {}".format(i, cost))

        if graph is True:
            plt.plot(np.arange(0, iterations + 1, step), costs)
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()

        return self.evaluate(X, Y)

    def save(self, filename):
        """Saves the instance object to a file in pickle format"""
        if not filename.endswith('.pkl'):
            filename += '.pkl'
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(filename):
        """
        Loads a pickled DeepNeuralNetwork object
        Returns the loaded pickle, or None if filename doesn’t exist
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None

    @staticmethod
    def sigmoid(Z):
        """Sigmoid Activation"""
        return 1 / (1 + np.exp(-Z))

    @staticmethod
    def sigmoid_derivative(A):
        """Sigmoid Derivative"""
        return A * (1 - A)
