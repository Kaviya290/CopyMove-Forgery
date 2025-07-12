from tkinter import *
import os
from tkinter import filedialog
import cv2

from tkinter import messagebox


def fulltraining():
    import model as mm


def testing():
    global testing_screen
    testing_screen = Toplevel(main_screen)
    testing_screen.title("Testing")
    # login_screen.geometry("400x300")
    testing_screen.geometry("600x450+650+150")
    testing_screen.minsize(120, 1)
    testing_screen.maxsize(1604, 881)
    testing_screen.resizable(1, 1)
    testing_screen.configure()
    # login_screen.title("New Toplevel")

    Label(testing_screen, text='''Upload Image''', width="300", height="2", font=("Palatino Linotype", 16)).pack()
    Label(testing_screen, text="").pack()
    Label(testing_screen, text="").pack()
    Label(testing_screen, text="").pack()
    Button(testing_screen, text='''Upload Image''', font=(
        'Palatino Linotype', 15), height="2", width="30", command=imgtest).pack()


def imgtest():
    global fffname

    import_file_path = filedialog.askopenfilename()

    image = cv2.imread(import_file_path)
    print(import_file_path)
    fffname = os.path.split(import_file_path)[1]
    filename = 'Output/Out/Test.jpg'
    cv2.imwrite(filename, image)
    print("After saving image:")

    result()


def result():
    print(fffname)
    import warnings
    warnings.filterwarnings('ignore')

    import tensorflow as tf
    classifierLoad = tf.keras.models.load_model('Model/model.h5')

    import numpy as np
    from keras.preprocessing import image
    test_image = image.load_img('./Output/Out/Test.jpg', target_size=(200, 200))
    # test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifierLoad.predict(test_image)

    out = ''
    if result[0][0] == 1:
        out = "Fake"

        messagebox.showinfo("Result", 'Fake')

    elif result[0][1] == 1:
        print("Orginal")
        out = "Orginal"
        messagebox.showinfo("Result", 'Orginal')

    if out == "Fake":
        my_new_string = fffname.replace("_F_", "_O_")
        print(my_new_string)
        img1 = cv2.imread("Data/Fake/" + fffname)
        img2 = cv2.imread("Data/Orginal/" + my_new_string)

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


def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = 600
    height = 500
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    # main_screen.geometry("300x250")
    main_screen.configure()
    main_screen.title("Copy Move Forgery Detection ")

    Label(text="Copy Move Forgery Detection ", width="300", height="5", font=("Palatino Linotype", 16)).pack()

    Button(text="Training", font=(
        'Palatino Linotype', 15), height="2", width="20", command=fulltraining, highlightcolor="black").pack(side=TOP)

    Label(text="").pack()
    Button(text="Testing", font=(
        'Palatino Linotype', 15), height="2", width="20", command=testing).pack(side=TOP)

    Label(text="").pack()

    main_screen.mainloop()


main_account_screen()
