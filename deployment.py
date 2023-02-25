'''
    #? to be able to see the web application,
    #? make sure to run this file using this command in terminal:
    ----------------------------------------
    #*    `streamlit run deployment.py`  
    ----------------------------------------
'''

import numpy as np
from tensorflow import keras
from keras import models
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

# reading data for normalization
(X_train, y_train), (X_test, y_test) = keras.datasets.boston_housing.load_data(path='boston-housing.npz',
                                                                               test_split=0.2, seed=113)

# normallize data
mms = MinMaxScaler()
mms.fit(X_train)
X_train = mms.transform(X_train)
X_test = mms.transform(X_test)

# load mode
model = models.load_model('house_price_predictor.h5')

# deployment
inputs_list = []

# all input labels
labels = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
          'DIS', 'RAD', 'TAX', 'PTRAITO', 'Black', 'LSTAT']

# all input explanations for ease of use.
captions = ['per capita crime rate by town',
            'proportion of residential land zoned for lots over 25,000',
            'proportion of non-retail business acres per town',
            'Charles River dummy variable',
            'nitric oxides concentration (parts per 10 million)',
            'average number of rooms per house',
            'proportion of owner-occupied units built prior to 1940',
            'weighted distances to five Boston employment centers',
            'index of accessibility to radial highways',
            'full-value property-tax rate per $10,000',
            'pupil-teacher ratio by town',
            'proportion of blacks by town',
            r'% lower status of the population']


def generate_input_vector(input_list):
    '''responsible for generatin input to the `model`.

    Parameters:
        input_list(list[float]): contains all inputs (CRIM, ZN. ...).

    Returns:
        input_vector(np.ndarray): contains the features that will be 
        fed to the `model`.
    '''

    X = np.array(input_list)
    feature_vector = mms.transform(X.reshape(1, -1))

    return feature_vector


def generate_number_input(label, caption, min_value=0.0):
    '''responsible for creating a UI `number_input` in streamlit package,
    and appending it to `inputs_list` variable

    Parameters:
        label(str): describe the label of the `number input`.
        caption(str): describe the explanation of the `number input`
        min_value(float) default=0.0: represents minimum value of the 
        `number input`
    '''

    st.caption(caption, unsafe_allow_html=False)
    number = st.number_input(label=label, min_value=min_value)
    inputs_list.append(number)


# for custom CSS style
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.header('House Price Prediciton')
with st.form(key='myform', clear_on_submit=False):
    col1, col2 = st.columns(2)  # divide screen to 2 columns
    with col1:
        # put the first 6 inputs in the first column
        for i in range(0, 6):
            generate_number_input(labels[i], captions[i])
            if i != 5:
                "---"
    with col2:
        # put the second 6 inputs in the second column
        for i in range(6, 12):
            generate_number_input(labels[i], captions[i])
            if i != 11:
                "---"

    # the last input of our 13 => "This done for symmetry design"
    "---"
    generate_number_input(labels[-1], captions[-1])

    submitted = st.form_submit_button(label='submit')
    if submitted:
        assert None not in inputs_list
        assert len(inputs_list) == 13

        X = generate_input_vector(inputs_list)
        prediction = model.predict(X)
        price = prediction[0][0] * 1000
        st.success(f"predicted price: {price:.2f} $")
