import numpy as np
import tensorflow as tf
import gzip

# Read Input data
LATENT_DIR = "./latent_files/"
ZIP_DIR = "./zip_files/"

# Initialize the input layer of the autoencoder
input_dim = 360
input_layer = tf.keras.layers.Input(shape=(input_dim,))

# Encoder architecture
encoder_layers = [360, 256, 128, 80, 64, 32, 16]
encoded = input_layer
for units in encoder_layers[1:]:
    encoded = tf.keras.layers.Dense(units, activation='relu')(encoded)

# Store the latent compressed data in a file
latent_data = tf.keras.Model(inputs=input_layer, outputs=encoded)
latent_data = latent_data.predict(input_data)
np.savetxt(LATENT_DIR+'latent_data.txt', latent_data)

# Compress the latent data using gzip
compressed_file = ZIP_DIR+'compressed_data.gz'
with gzip.open(compressed_file, 'wb') as f:
    np.savetxt(f, latent_data)

# Load the compressed data
with gzip.open(compressed_file, 'rb') as f:
    latent_data = np.loadtxt(f)

# Decoder architecture
decoder_layers = [256, 128, 80, 64, 32, 16, input_dim]
decoded = latent_data
for units in decoder_layers:
    decoded = tf.keras.layers.Dense(units, activation='relu')(decoded)

# Save the output of the decoder layer after the 256 neuron layer
output_file = 'decoder_output.txt'
decoder_output = tf.keras.Model(inputs=input_layer, outputs=decoded)
decoded_output = decoder_output.predict(input_data)
np.savetxt(output_file, decoded_output)

# Decompress the file
decompressed_data = []
with gzip.open(output_file, 'rb') as f:
    for line in f:
        decompressed_data.append(line.decode().strip())
decompressed_data = np.array(decompressed_data, dtype=float)

# Input the decompressed data to a layer with 300 neurons
input_layer_300 = tf.keras.layers.Input(shape=(input_dim,))
layer_300 = tf.keras.layers.Dense(300, activation='relu')(input_layer_300)
# Continue with the rest of the layers in the decoder architecture

# Autoencoder model
autoencoder = tf.keras.Model(inputs=input_layer_300, outputs=decoded)

# Compile and train the model
autoencoder.compile(optimizer='adam')
autoencoder.fit(decompressed_data, decompressed_data, epochs=800, batch_size=32)
