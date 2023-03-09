
from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import  preprocess_input
import numpy as np
import cv2 as cv
from PIL import Image
import base64
import pymongo
from io import BytesIO
connection_string = "mongodb+srv://rap:rap@cluster0.3iayb.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)

# Access a database and collection
db = client.RapAssignment
collection = db.image
model = tf.keras.models.load_model('document_class15-epoch.model')

app = Flask(__name__)

# Define a route for the upload form
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    image_file = request.files['rapidvs']
    if image_file:
       
        image_data = image_file.read()
        image_doc = {"image": base64.b64encode(image_data).decode()}
 
        image_id = collection.insert_one(image_doc).inserted_id
     
        image_loc = collection.find_one({"_id":image_id})
        if image_loc is not None and "image" in image_loc:
        
            nparr = np.frombuffer(base64.b64decode(image_loc["image"]), np.uint8)
            image = Image.open(BytesIO(nparr))
            target_shape=(700,1000,3)
            image_array =np.array(image)
            img_resi=np.resize(image_array,target_shape)
            
          
           
            x = img_resi
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            predictions = model.predict(x)
            result_class = np.argmax(predictions, axis = -1)
            prob=predictions[0][result_class]

            if result_class == 0:
                pred='Email'
            elif result_class == 1:
                pred='Resume'
            else :
                pred='Scientic Publication'

        return render_template('success.html', prediction=pred,probability=prob)

if __name__ == '__main__':
    app.run(debug=True)
