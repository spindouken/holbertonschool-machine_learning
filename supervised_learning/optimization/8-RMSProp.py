#!/usr/bin/env python3
"""
creates the training operation for a neural network in tensorflow
using the RMSProp optimization algorithm
"""
import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """
    loss: loss of the network
    alpha: learning rate
    beta2: RMSProp weight
    epsilon: small number to avoid division by zero
    Returns the RMSProp optimization operation
    """
    optimizer = tf.train.RMSPropOptimizer(alpha, decay=beta2, epsilon=epsilon)
    train_op = optimizer.minimize(loss)
    return train_op
