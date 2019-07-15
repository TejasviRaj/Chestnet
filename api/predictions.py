from sklearn.metrics import confusion_matrix
import time
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from keras import backend as K
from keras.applications.densenet import DenseNet121
from keras.layers import Dense, Input
from keras.models import Model as Md
from keras import optimizers
from skimage.transform import resize

import numpy as np

from PIL import Image

m=None

def predict(file_name):
    #if (not m):
    # global m
    # if (not m):
    m=Model()
    print ("from predictions",file_name)
    return (m.predict(file_name))


class Model:
    def __init__(self):
        K.clear_session()
        base_model = DenseNet121(include_top=False,input_tensor=Input(shape=(224, 224, 3)),input_shape=(224, 224, 3), weights="imagenet",pooling="avg")
        x = base_model.output
        predictions = Dense(14, activation="sigmoid", name="predictions")(x)
        self.model = Md(inputs=base_model.input, outputs=predictions)
        optimizer = optimizers.Adam(lr=0.001, decay=1e-6)
        self.model.compile(optimizer=optimizer, loss="binary_crossentropy")
        self.model.load_weights("weight.h5")
        self.class_names=["Atelectasis","Cardiomegaly","Effusion","Infiltration","Mass","Nodule","Pneumonia","Pneumothorax","Consolidation","Edema","Emphysema","Fibrosis","Pleural_Thickening","Hernia"]
        self.threshold ={"Atelectasis":0.10022616982460021973,"Cardiomegaly":4.9802322387695312e-12,"Effusion":5.1021575927734375e-01,"Infiltration":0.103368943929672241,"Mass":2.115964889526367e-25,"Nodule":7.718801498413086e-06,"Pneumonia":5.960464477539063e-1,"Pneumothorax":2.980232238769531e-02,"Consolidation":6.467103958129883e-05,"Edema":2.9802322387695312e-08,"Emphysema":2.9802322387695312e-08,"Fibrosis":2.9802322387695312e-08,"Pleural_Thickening":3.2782554626464844e-07,"Hernia":0.5}

    def predict(self,file_name):
        print("from predict", file_name)

        im=self.load_image(file_name)
        im=self.transform_batch_images(im)
        p = self.model.predict(im)

        counter = 0
        diseases = []

        for i in self.class_names:
          if p[0][counter]>=self.threshold[i]:
            diseases.append(i)
          counter = counter+1
        return diseases

    def load_image(self, image_file):
        image = Image.open(image_file)
        image_array = np.asarray(image.convert("RGB"))
        image_array = resize(image_array, (224,224))
        image_array = image_array / 255.
        image_array = image_array.reshape((1,224,224,3))
        return image_array

    def transform_batch_images(self, batch_x):
        imagenet_mean = np.array([0.485, 0.456, 0.406])
        imagenet_std = np.array([0.229, 0.224, 0.225])
        batch_x = (batch_x - imagenet_mean) / imagenet_std
        return batch_x