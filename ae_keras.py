from keras.models import Model
from keras.layers import Dense, Embedding, Input, concatenate, Reshape, RepeatVector
from keras.layers import LSTM, Bidirectional, GlobalMaxPool1D, Dropout, BatchNormalization, Conv2D
from keras.preprocessing import text, sequence



def AE(timesteps = 10, input_dim = 50, embed_max_features = 50000, embed_size = 128, latent_dim=30):
    inputs = Input(shape=(input_dim,))
    embed = Embedding(embed_max_features, embed_size)(inputs)
    encoded = LSTM(latent_dim)(embed)

    decoded = RepeatVector(timesteps)(encoded)
    decoded = LSTM(input_dim, return_sequences=True)(decoded)
    #embed_decoded = Embedding(embed_max_features, embed_size)(decoded)
    #embed_flatten = Flatten()(embed_decoded)
    embed_flatten = Flatten()(embed)
    decoded = Dense(input_dim)(inputs)

    sequence_autoencoder = Model(inputs, decoded)
    sequence_autoencoder.compile(loss='mae', optimizer='adam')#, metrics=['accuracy'])
    #encoder = Model(inputs, encoded)
    return sequence_autoencoder

