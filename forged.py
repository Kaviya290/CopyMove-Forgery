import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# set path to dataset
dataset_path = "CoMoFoD_small_v2"

# set parameters for data processing
image_size = 100
num_classes = 2

# create lists to store data and labels
data = []
labels = []

# load dataset and extract features
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.endswith(".png"):
            # read image
            img = cv2.imread(os.path.join(root, file))
            # extract label
            if "_F_" in file:
                labels.append(1)
                print(file)
                cv2.imwrite('Fake/'+file,img)

            elif "_O_" in file:
                labels.append(0)
                cv2.imwrite('Orginal/' + file, img)

# convert lists to arrays
'''data = np.array(data)
labels = np.array(labels)

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)


print(X_train)
print(X_test)

print(y_train)
print(y_test)
# build CNN model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(image_size, image_size, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='sigmoid'))

# compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# train model
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# evaluate model
score = model.evaluate(X_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

# plot training and validation accuracy and loss
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()'''