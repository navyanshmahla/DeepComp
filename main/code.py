import numpy as np
import tensorflow as tf
from sklearn.cluster import KMeans
from gzip import *


OUTPUT_DIR = "./zip_files/"
LATENT_DIR = "./latent_files/"
LATENT_FILE_NAME = "latent_data.txt"

# Initialize the input layer of the autoencoder
input_dim = 360
input_layer = tf.keras.layers.Input(shape=(input_dim,))

# Encoder architecture
encoder_layers = [256, 128, 80, 64, 32, 16]
encoded = input_layer
for units in encoder_layers:
    encoded = tf.keras.layers.Dense(units, activation='relu')(encoded)

# Create a model to get the bottleneck/latent representation
encoder = tf.keras.Model(inputs=input_layer, outputs=encoded)

# Store the latent compressed data in a file
latent_data = encoder.predict(input_data)
np.savetxt(LATENT_DIR+LATENT_FILE_NAME, latent_data)
compress_file(LATENT_DIR+LATENT_FILE_NAME, './zip_files')

# Load the latent data from the file
latent_data = np.loadtxt('./latent_files/latent_data.txt')

# Decoder architecture
decoder_layers = [16, 32, 64, 80, 128, 256, input_dim]
decoded = latent_data
for units in decoder_layers:
    decoded = tf.keras.layers.Dense(units, activation='relu')(decoded)

# Autoencoder model
autoencoder = tf.keras.Model(inputs=latent_input, outputs=decoded)

# Compile and train the model
autoencoder.compile(optimizer='adam')
autoencoder.fit(latent_data, input_data, epochs=800, batch_size=32)
