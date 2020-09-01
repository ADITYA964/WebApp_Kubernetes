import streamlit as st
import tensorflow as tf 
from PIL import Image
import numpy as np

## Load model
model = tf.keras.models.load_model('Models/resnetv1')

## Label dictionary
label_dict = {'Buildings': 0,
            'Forest': 1,
            'Glacier': 2,
            'Mountain': 3,
            'Sea': 4,
            'Street': 5}

## Prediction function
def predict_img(img):
    img = img.resize((150,150)) # resize image
    img_array = np.asarray(img).reshape((1,150,150,3))/255 # normalize
    pred = model.predict(img_array) # predict
    img_label = list(label_dict.keys())[np.argmax(pred)] # get label
    return img_label 

## Streamlit app builder
st.sidebar.title('About') 
# Info
st.sidebar.info('This app classifies 6 types of scenes: Buildings, Forests, Glaciers, Mountains, Sea, Street')
# File uploader
uploaded_file = st.sidebar.file_uploader("Choose an image [JPG or PNG]", type=['jpg','png'])
# run prediction
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    label = predict_img(image)
    st.image(image, caption = 'Prediction:' + label)