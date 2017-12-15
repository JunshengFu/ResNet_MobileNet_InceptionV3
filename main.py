from keras.preprocessing import image
import numpy as np

#-----ResNet50--------#
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

#-----Mobilenet-------#
from keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions

#-----InceptionV3-----#
from keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions


# 1: ResNet50, 2: MobileNet, 3: InceptionV3
choice = 3

if choice == 1:
    model = ResNet50(weights='imagenet')
elif choice == 2:
    model = MobileNet(weights='imagenet')
else:
    model = InceptionV3(weights='imagenet')


# give the path of the input image
img_path = 'light1.jpg'

# shape the image size to 224x224
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# decode the results into a list of tuples (class, description, probability)
preds = model.predict(x)

# print the top 3 guesses
print('Predicted:', decode_predictions(preds, top=3)[0])
