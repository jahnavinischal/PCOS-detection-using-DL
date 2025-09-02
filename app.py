import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__ ,template_folder='template')
from keras.models import load_model, model_from_json
from tensorflow import keras
# from skimage.transform import resize
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
IMG_FOLDER = os.path.join( './uploads')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
print("Loading model")
global json_file
json_file = open('model1.json', 'r')
global loaded_model_json
loaded_model_json = json_file.read()
json_file.close()
global loaded_model
loaded_model = model_from_json(loaded_model_json)


loaded_model.load_weights("model1.weights.h5")

global model
model=loaded_model


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/reports', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        print(filename)
        return redirect(url_for('prediction', filename=filename))
    # return render_template('pass.html',filename=filename)
    return render_template('reports.html')

@app.route('/faq')
def faq_page():
    return render_template('faq.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/clinical')
def clinical_page():
    return render_template('clinical.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/prediction/<filename>')
def prediction(filename):
    import cv2
    my_image = cv2.imread(os.path.join('uploads', filename), cv2.COLOR_BGR2RGB)
    print("Shape:",my_image.shape)
    my_image_re = cv2.resize(my_image, (224,224))
    my_image_re=np.expand_dims(my_image_re,axis=0)
    prediction = model.predict(my_image_re)

    print(prediction)
   
    value = np.argmax(prediction,axis=-1)
    print("Value",value)
   
    result ='PCOS'
    if (value[0]==1):
        print("PCOS Detected")
        result = 'PCOS detected'
    elif(value[0]==0):
        print("PCOS not detected")
        result = 'PCOS not detected'
    
    print(result)

    return render_template('pass.html', predictions=result)
app.run(host='0.0.0.0', port=80)



