import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.utils import *
from tensorflow.keras.callbacks import *
from tensorflow.keras.initializers import *
from tensorflow.keras.applications import vgg16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D, GlobalAveragePooling2D 
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Model, Sequential
from keras.optimizers import Adam, RMSprop
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import SGD
import tensorflow as tf
import os
import pandas as pd
import seaborn as sn
import numpy as np

MODEL_NAME = 'VGG16'
DATASET_NAME = 'FER2013_oversampling'
EPOCHS = 100


os.mkdir(MODEL_NAME + '_'+ DATASET_NAME)


CATEGORIES = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
X = []
y = []
#data = pd.read_csv('../datasets/FER2013/fer2013.csv')
data = pd.read_csv('../datasets/FER2013/fer2013_oversampled.csv')

#check data shape
data.shape

emotion_map = {0: 'Angry', 1: 'Digust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}
emotion_counts = data['emotion'].value_counts(sort=False).reset_index()
emotion_counts.columns = ['emotion', 'number']
emotion_counts['emotion'] = emotion_counts['emotion'].map(emotion_map)



for index, row in data.iterrows():
    try:
        pixels=np.asarray(list(row['pixels'].split(' ')), dtype=np.uint8)
        img = pixels.reshape((48,48))
        X.append(img)
        y.append(row['emotion'])
    except Exception as e:
        pass

X = np.array(X, dtype='float32').reshape(-1, 48, 48)
rgb_X = np.repeat(X[..., np.newaxis], 3, -1)
rgb_X=rgb_X/255.
y = np.asarray(y)
y.shape

(X_train, X_val, y_train, y_val) = train_test_split(rgb_X, y,
                                                    test_size=0.2,
                                                    random_state=2022,
                                                    shuffle=True,
                                                    stratify=y)
aug_train = ImageDataGenerator(
    rotation_range=20,
    zoom_range=0.15,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.15,
    horizontal_flip=True,
    fill_mode="nearest")

generator_val = ImageDataGenerator()


aug_train.fit(X_train)

generator_val.fit(X_val)

IMG_WIDTH = 48
IMG_HEIGHT = 48


model = Sequential()

pretrained_model = vgg16.VGG16(include_top=False, 
                                        input_shape=(IMG_WIDTH, IMG_HEIGHT, 3),classes=7,
                                        weights='imagenet')

model.add(pretrained_model)
#model.add(Flatten())
model.add(GlobalAveragePooling2D())
model.add(Dropout(0.2))
# Output layer
model.add(Dense(7, activation='softmax'))
# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001),loss=tf.keras.losses.SparseCategoricalCrossentropy(),metrics=['accuracy'])
model.summary()


# Train the model

early_stopping = EarlyStopping(
    monitor = 'val_accuracy',
    mode = 'auto',
    min_delta = 0.0001,
    patience = 7,
    baseline = None,
    restore_best_weights = True,
    verbose = 1
)

save_path = MODEL_NAME + '_'+ DATASET_NAME +'/'+ MODEL_NAME + '_'+ DATASET_NAME +'.h5'
checkpoint = ModelCheckpoint(
    save_path,
    monitor = 'val_accuracy',
    mode = 'max',
    save_best_only = True,
    save_weights_only= False ,
    perior = 1,
    verbose = 1
)


learning_rate_reduction = ReduceLROnPlateau(monitor='val_accuracy', 
                                            patience=3,                                             
                                            verbose=1, 
                                            factor=0.5, 
                                            min_lr=0.00001)

history = model.fit_generator(aug_train.flow(X_train, y_train, batch_size=32),
                    validation_data=generator_val.flow(X_val, y_val, batch_size=32),
                    steps_per_epoch=len(y_train) // 32,
                    epochs=EPOCHS,
                    callbacks=[early_stopping, checkpoint, learning_rate_reduction])




fig, axes = plt.subplots(1,2, figsize=(18, 6))
# Plot training & validation accuracy values
axes[0].plot(history.history['accuracy'])
axes[0].plot(history.history['val_accuracy'])
axes[0].set_title('Model accuracy')
axes[0].set_ylabel('Accuracy')
axes[0].set_xlabel('Epoch')
axes[0].legend(['Train', 'Validation'], loc='upper left')

# Plot training & validation loss values
axes[1].plot(history.history['loss'])
axes[1].plot(history.history['val_loss'])
axes[1].set_title('Model loss')
axes[1].set_ylabel('Loss')
axes[1].set_xlabel('Epoch')
axes[1].legend(['Train', 'Validation'], loc='upper left')
plt.savefig(MODEL_NAME + '_'+ DATASET_NAME +'/'+ 'acc_loss.png')

#plt.show()

predicted_label = model.predict(X_val)
predicted_label = np.argmax(predicted_label, axis = 1)

#cm  = confusion_matrix(y_val, predicted_label)
#plot_confusion_matrix(cm,figsize=(8,8), cmap=plt.cm.Blues, colorbar=True, class_names=CATEGORIES)
#plt.show()

cm = confusion_matrix(y_val, predicted_label)
# Normalise
cmn = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
fig, ax = plt.subplots(figsize=(8,8))
sn.heatmap(cmn, annot=True, fmt='.2f', cmap=plt.cm.Blues, xticklabels=CATEGORIES, yticklabels=CATEGORIES)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.savefig(MODEL_NAME + '_'+ DATASET_NAME +'/'+ 'conf_matrix.png')

#plt.show()

