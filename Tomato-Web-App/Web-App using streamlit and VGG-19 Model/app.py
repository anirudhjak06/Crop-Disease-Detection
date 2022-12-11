import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

def prepare(file):
    #img_array=cv2.imread(filepath,cv2.IMREAD_COLOR)
    img_array=file/255
    #new_array=cv2.resize(img_array,(128,128))
    return img_array.reshape(-1,128,128,3)

class_dict={'Tomato Bacterial spot': 0,
            'Tomato Early blight': 1,
            'Tomato Late blight': 2,
            'Tomato Leaf Mold': 3,
            'Tomato Septoria leaf spot': 4,
            'Tomato Spider mites Two-spotted spider mite': 5,
            'Tomato Target Spot': 6,
            'Tomato Tomato Yellow Leaf Curl Virus': 7,
            'Tomato Tomato mosaic virus': 8,
            'Tomato healthy': 9}

def prediction_cls(prediction):
    for key, clss in class_dict.items():
        if np.argmax(prediction)==clss:
            return key


@st.cache
def load_image(image_file):
    img=Image.open(image_file)
    img=img.resize((128,128))
    return img
    pass

def main():
    st.image("./img2.jpg",use_column_width=True)


    st.title("Tomato Disease Prediction")
    st.subheader("Please upload the Tomato leaf image : ")
    image_file=st.file_uploader("Upload Image",
                                type=["png","jpg","jpeg"])
    if st.button("Process"):
        img=load_image(image_file)
        st.image(img,caption="Uploaded Image")
        img=tf.keras.preprocessing.image.img_to_array(img)
        model=tf.keras.models.load_model("model_vgg19.h5")
        #print(img)
        img=prepare(img)
        #print(img)
        st.subheader(prediction_cls(model.predict(img)))

    pass

if __name__=="__main__":
    main()