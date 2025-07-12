import cv2
import numpy as np
import warnings

warnings.filterwarnings('ignore')

import tensorflow as tf

classifierLoad = tf.keras.models.load_model('model.h5')

import numpy as np
from keras.preprocessing import image

test_image = image.load_img('./Data/Fake/003_F_BC2.png', target_size=(200, 200))
test_image = np.expand_dims(test_image, axis=0)
result = classifierLoad.predict(test_image)

out = ''
if result[0][0] == 1:
    print("Fake")
    out ='Fake'

elif result[0][1] == 1:
    print("Orginal")
    out = 'Orginal'


if out=="Fake":



    img1 = cv2.imread("Data/Fake/003_F_BC2.png")
    img2 = cv2.imread("Data/Orginal/003_O_BC2.png")

    # Convert the images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the two images
    diff = cv2.absdiff(gray1, gray2)

    #  the difference image
    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]

    # Find contours in the thresholded image
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # _, contours, _= cv2.findContours(skin_ycrcb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a rectangle around each contour
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the result
    cv2.imshow("Result", img1)
    cv2.imshow("orginal", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


