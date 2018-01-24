from keras.models import Model
from keras.layers import Dense, Embedding, Input, concatenate, Reshape, RepeatVector
from keras.layers import LSTM, Bidirectional, GlobalMaxPool1D, Dropout, BatchNormalization, Conv2D
from keras.preprocessing import text, sequence



def ae(timesteps, input_dim, embed_max_features, embed_size):
    inputs = Input(shape=(timesteps, input_dim))
    embed = Embedding((embed_max_features, embed_size))(inputs)
    encoded = LSTM(latent_dim)(embed)
    
    decoded = RepeatVector(timesteps)(encoded)
    decoded = LSTM(input_dim, return_sequences=True)(decoded)
    embed_decoded = Embedding((embed_max_features, embed_size))(decoded)
    decoded = Dense(input_dim)(embed_decoded)

    sequence_autoencoder = Model(inputs, decoded)
    sequence_autoencoder.compile(loss='mae', optimizer='adam')#, metrics=['accuracy'])
    #encoder = Model(inputs, encoded)
    return sequence_autoencoder
