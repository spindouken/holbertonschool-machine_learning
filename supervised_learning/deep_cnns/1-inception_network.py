#!/usr/bin/env python3
"""
Builds inception network as described in Going Deeper with Convolutions (2014)
"""
import tensorflow.keras as K
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """
    Returns: the keras model
    """
    input_layer = K.Input(shape=(224, 224, 3))

    conv_7x7 = K.layers.Conv2D(filters=64,
                               padding='same',
                               activation='relu',
                               kernel_size=(7, 7),
                               strides=(2, 2))(input_layer)
    maxpool_3x3_1 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                          strides=(2, 2),
                                          padding='same')(conv_7x7)

    conv_3x3 = K.layers.Conv2D(filters=192,
                               kernel_size=(3, 3),
                               strides=(1, 1),
                               padding='same',
                               activation='relu')(maxpool_3x3_1)
    maxpool_3x3_2 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                          strides=(2, 2),
                                          padding='same')(conv_3x3)

    inception_3a = inception_block(maxpool_3x3_2, (64, 96, 128, 16, 32, 32))
    inception_3b = inception_block(inception_3a, (128, 128, 192, 32, 96, 64))
    maxpool_3x3_3 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                          strides=(2, 2),
                                          padding='same')(inception_3b)
    inception_4a = inception_block(maxpool_3x3_3, (192, 96, 208, 16, 48, 64))
    inception_4b = inception_block(inception_4a, (160, 112, 224, 24, 64, 64))
    inception_4c = inception_block(inception_4b, (128, 128, 256, 24, 64, 64))
    inception_4d = inception_block(inception_4c, (112, 144, 288, 32, 64, 64))
    inception_4e = inception_block(inception_4d, (256, 160, 320, 32, 128, 128))
    maxpool_3x3_4 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                          strides=(2, 2),
                                          padding='same')(inception_4e)
    inception_5a = inception_block(
        maxpool_3x3_4, (256, 160, 320, 32, 128, 128))
    inception_5b = inception_block(inception_5a, (384, 192, 384, 48, 128, 128))
    avg_pool_7x7 = K.layers.AveragePooling2D(pool_size=(7, 7),
                                             strides=(1, 1),
                                             padding='valid')(inception_5b)

    dropout_40 = K.layers.Dropout(rate=(0.4))(avg_pool_7x7)
    output = K.layers.Dense(units=(1000), activation='softmax')(dropout_40)

    model = K.Model(inputs=input_layer, outputs=output)
    model.compile(optimizer=K.optimizers.Adam(),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model
