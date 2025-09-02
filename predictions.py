import numpy as np
import tensorflow as tf
from keras.preprocessing import image
model = tf.keras.models.load_model("model.h5")
categories = ["Ain","Al","Alef","Beh","Dad","Dal","Feh","Ghain","Hah","Heh","Jeem","Kaf","Khah","Laa","Lam","Meem",
              "Noon","Qaf","Reh","Sad","Seen","Sheen","Tah","Teh","Teh_Marbuta","Thal","Theh","Waw","Yeh","Zah","Zain"]
def predict(img):
    size = 224
    temp_img = image.load_img(img, target_size=(size, size))
    x = image.img_to_array(temp_img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    prediction = np.argmax(model.predict(images), axis=1)
    prediction_str = categories[prediction.item()]
    return prediction_str