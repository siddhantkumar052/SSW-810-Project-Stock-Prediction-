#810 Project - Stock Prediction Using Python
#Contributers: Shivank Srivastava (20006832), Siddhantkumar Maske (20006862)

'This code contains the program to run prediction and train model'
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import datetime
import yfinance as yf
import numpy as np
from keras.models import load_model
import streamlit as st

def ml_model();
#ML Model

    from keras.layers import Dense, Dropout, LSTM
    from keras.models import Sequential

    model = Sequential()
    model.add(LSTM(units = 50, activation = 'relu', return_sequences = True, input_shape = (x_train.shape[1], 1) ))
    model.add(Dropout(0.2))

    model.add(LSTM(units = 60, activation = 'relu', return_sequences = True))
    model.add(Dropout(0.3))

    model.add(LSTM(units = 80, activation = 'relu', return_sequences = True))
    model.add(Dropout(0.4))

    model.add(LSTM(units = 120, activation = 'relu'))
    model.add(Dropout(0.5))

    model.add(Dense(units = 1))

    print(model.summary())

    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    model.fit(x_train, y_train, epochs = 50)

    model.save('keras_model.h5')
    #model is exported and used in the main program


